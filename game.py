#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys
import scenes as s
import inventory as i
import os


def clear(): return os.system('cls')


def signal_handler(signal, frame):
    """Handle a control-c."""
    print("\n\nExiting - hope you enjoyed playing :)\n")
    sys.exit(0)


# Uncomment this for CLI use
#signal.signal(signal.SIGINT, signal_handler)

#############################################################################
#                              Intro Banner
#############################################################################


def banner(text, ch='=', length=78):
    spaced_text = ' %s ' % text
    return spaced_text.center(length, ch)


title = '''
   _____ __                                      __
  / ___// /__________ ___  __   ________  ____ _/ /___ ___  _____
  \__ \/ __/ ___/ __ `/ / / /  / ___/ _ \/ __ `/ / __ `__ \/ ___/
 ___/ / /_/ /  / /_/ / /_/ /  / /  /  __/ /_/ / / / / / / (__  )
/____/\__/_/   \__,_/\__, /  /_/   \___/\__,_/_/_/ /_/ /_/____( )
                    /____/                                    |/
   __  __            _____             __   __
  / /_/ /_  ___     / __(_)___  ____ _/ /  / /_  ____  __  _______
 / __/ __ \/ _ \   / /_/ / __ \/ __ `/ /  / __ \/ __ \/ / / / ___/
/ /_/ / / /  __/  / __/ / / / / /_/ / /  / / / / /_/ / /_/ / /
\__/_/ /_/\___/  /_/ /_/_/ /_/\__,_/_/  /_/ /_/\____/\__,_/_/

'''
authors = "Skary Sneks"

# Pick font from: http://www.figlet.org/examples.html
print('')
print('')
print('Welcome to:')
print (title)
print(banner('by: {0}, 2017'.format(authors)))
print('')

#############################################################################
#                      Game Constants: Weapons, s.Scenes etc.
#############################################################################

# Game Constants
global game
game = {
    "scene": None,
    "score": 0,
    "health": 100,
    "inventory": [
        i.INVENTORY_POTION,
        i.INVENTORY_SWORD
    ],
    "finished": False,
}

#############################################################################
#                              Game Functions
#############################################################################


def help():
    """Print help!"""
    print('''
    #################################################
    # HELP! you can run these commands at any time: #
    #                                               #
    #    inventory: show your inventory             #
    #    game:      display current game stats      #
    #    quit:      save and quits                  #
    #                                               #
    #################################################
    ''')


def print_inventory_item(item):
    """Prints a formatted individual inventory item."""
    print('{0}: (id: {1})'.format(item['name'], item['id']))
    print("\tRemaining use: {0}".format(item['use']))
    print("\tDamage: {0}".format(item['damage']))
    print("\tHealth: {0}".format(item['health']))


def print_inventory():
    """Prints a formatted list of inventory items."""
    print(banner('inventory: '))
    for i in game['inventory']:
        print_inventory_item(i)
    print('\n')


def print_game_status():
    print(banner('game status: '))
    print('Score: {0}: '.format(game['score']))
    print('Health: {0}: '.format(game['health']))
    print('\n')


def do_menu_action(action):
    """Execute menu action!"""
    return {
        'help': help,
        'inventory': print_inventory,
        'game': print_game_status,
        'quit': save_game,
    }.get(action, (lambda: ''))()


def load_scene(scene):
    """Loads a scene by id into the current game scene."""
    game['scene'] = s.scenes[scene]


def is_finished():
    """Detect if game is finished."""
    return game['finished']


def scene_is_battle(scene):
    """Detect if current scene is a battle."""
    return scene['type'] is s.SCENE_TYPE_BATTLE


def scene_is_inventory(scene):
    """Detect if current scene is an Inventory scene to collect an item."""
    return scene['type'] is s.SCENE_TYPE_INVENTORY


def start_game():
    """Starts the game!"""
    new_or_existing = raw_input(
        '''Would you like to start a new game (n) or open an existing (o)? ''')
    load_scene(0)

    if new_or_existing == 'o':
        load_game()

    print('Starting game from scene {0}'.format(game["scene"]["name"]))


def load_game():
    """Load a game from file."""
    print('ERROR: loading a game not currently supported')
    return

    file_name = raw_input("Enter file to open: ")
    print("Reading game from file {0}".format(file_name))
    with open(file_name, 'r') as f:
        global game
        game = load(f)


def save_game():
    """Save a game from file."""
    print('ERROR: saving a game not currently supported')
    return

    file_name = raw_input("Filename: ")
    print("Saving game to file {0}".format(file_name))
    with open(file_name, 'w') as f:
        dump(game, f)


def die():
    """You dead!"""
    game['health'] = 0
    game['finished'] = True


def win():
    """You have won!!!"""
    game['finished'] = True


def find_inventory_item_by_id(item):
    """Find an item from an inventory by its id."""
    for i, x in enumerate(game['inventory']):
        if x['id'] is item:
            return i, x
    return -1, None


def battle_boss(move):
    """Apply a move to the current boss."""
    # Damage the boss
    game['scene']['health'] -= move['damage']

    # Decrement the inventory item
    i, _ = find_inventory_item_by_id(move['id'])
    game['inventory'][i]['use'] -= 1

    if game['inventory'][i]['use'] <= 0:
        del game['inventory'][i]
        print('You have run out of {0} '.format(move['name']))


def is_boss_dead():
    """Check if boss is dead."""
    return game['scene']['health'] <= 0


def am_i_dead():
    """Check if I am dead."""
    return game['health'] <= 0


def game_over(reason='You are dead'):
    """Game over!"""
    print("{0} - GAME OVER!".format(reason))


def inventory():
    """Collect inventory."""
    scene = game['scene']
    item = scene['item']

    print('You have collected a new item: ')
    print_inventory_item(item)
    game['inventory'].append(item)

    # Go to default choice
    return game['scene']['choices'][0]['scene']


def battle():
    """Battle!"""
    scene = game['scene']
    boss = scene['boss']
    boss_damage = scene['damage']

    print("You are now about to battle {0}, who fights with damage {1}.".format(
        scene['boss'], boss_damage))

    # Logic
    #   - Turn based game, player gets to move first
    #   - At any point in time, you can call help functions to see what's happening
    #   - When you run out of inventory or health AND your opponent is not dead, you die - GAME OVER
    battling = True

    while battling:
        boss_health = scene['health']
        inventory = game['inventory']

        print('{0} has health:  {1}'.format(boss, boss_health))
        print('You have health: {0}\n'.format(game['health']))
        print('You have the following moves available: \n')
        print_inventory()

        answer = raw_input('Select your move (by id): ')
        try:
            if len(inventory) <= 0:
                game_over('You have run out of moves!')

            elif int(answer) in map((lambda x: x['id']), inventory):
                _, move = find_inventory_item_by_id(int(answer))
                print('You chose {0} and inflict {1} damage'.format(
                    move['name'], move))

                # Apply move (to self or boss)
                # Decrease inventory use by 1
                battle_boss(move)

                # Check - are we still alive?
                if am_i_dead():
                    game_over()
                    battling = False

                # Check - is the opponent still alive?
                if is_boss_dead():
                    print('You defeated {0}!'.format(boss))
                    # Go to the post-battle scene
                    return game['scene']['choices'][0]['scene']
                else:
                    # Boss applies move against you!
                    print('{0} {1} and inflicts {2} damage'.format(
                        boss, game['scene']['weapon'], game['scene']['damage']))
                    game['health'] -= game['scene']['damage']
                    if am_i_dead():
                        battling = False
                        game_over()

            else:
                print("Invalid answer. ")
        except ValueError:
            do_menu_action(answer)


def display_scene():
    """Display a scene."""
    scene = game['scene']
    print(
        "\n" + banner('You make your way to {0} ...'.format(scene['name'])) + "\n")

    if scene_is_battle(scene):
        load_scene(battle())
    elif scene_is_inventory(scene):
        load_scene(inventory())
    else:
        print(scene['description'] + '\n\n')
        answered = False

        while answered is False:
            for option in scene['choices']:
                print('{0}: {1}'.format(
                    option['scene'], option['description']))
            answer = raw_input('\nHow will you proceed? ')
            try:
                if int(answer) in map((lambda x: x['scene']), scene['choices']):
                    answered = True
                else:
                    print("Invalid answer. ")
            except ValueError:
                do_menu_action(answer)

        load_scene(int(answer))


#############################################################################
#                              Main game logic!
#############################################################################

# 1. New Game or load existing?
start_game()

# 2. Display scene
while True:
    if is_finished is True and am_i_dead:
        print("Game Over!")
        exit(0)
    elif is_finished is True:
        win()
    else:
        display_scene()
