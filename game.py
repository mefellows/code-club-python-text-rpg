#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from pyfiglet import figlet_format
#from pickle import load, dump
from enum import Enum
import signal
import sys


def signal_handler(signal, frame):
    """Handle a control-c."""
    print("\n\nExiting - hope you enjoyed playing :)\n")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

#############################################################################
#                              Intro Banner
#############################################################################


def banner(text, ch='=', length=78):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner


title = "Stray realms, the final hour"
authors = "Skary Sneks"

# Pick font from: http://www.figlet.org/examples.html
print('')
print('')
print('Welcome to:')
#print(figlet_format(title, font='slant'))
print (title)
print(banner('by: {0}, 2017'.format(authors)))
print('')

#############################################################################
#                      Game Constants: Weapons, Scenes etc.
#############################################################################

# Game Constants
INFINITY = float("inf")

# Possible inventory items
INVENTORY_POTION = {
    "id": 0,
    "name": "Magic potion",
    "damage": 0,
    "health": 25,
    "use": 5
}

INVENTORY_SWORD = {
    "id": 1,
    "name": "Enchanted sword",
    "damage": 2,
    "health": 0,
    "use": INFINITY
}

# Scene types
SCENE_TYPE_SCENE = 0
SCENE_TYPE_BATTLE = 1

scenes = [
    {
        "name": "some amazing scene",
        "type": SCENE_TYPE_SCENE,
        "description": """some amazing description of this scene, this will be elaborated on
                      when the scene shows up, and may contain ASCII pictures!
                      """,
        "choices": [
            {
                "scene": 1,
                "description": "Head North to the castle"
            }
        ]
    },
    {
        "name": "the castle",
        "type": SCENE_TYPE_SCENE,
        "description": '''
                              o
                          _---|         _ _ _ _ _
                       o   ---|     o   ]-I-I-I-[
      _ _ _ _ _ _  _---|      | _---|    \ ` ' /
      ]-I-I-I-I-[   ---|      |  ---|    |.   |
       \ `   '_/       |     / \    |    | /^\|
        [*]  __|       ^    / ^ \   ^    | |*||
        |__   ,|      / \  /    `\ / \   | ===|
     ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
     I_I__I_I__I_I  (====(_________)___|_|____|____
     \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|
      |[]      '|   | []  |`__  . [  \-\--|-|--/-/
      |.   | |' |___|_____I___|___I___|---------|
     / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
    <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \
    ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>
    ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [
    <===>     ' ||||| |   |   | ||||.||  []   <===>
     \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/
      |      . _||||| |   |   | ||||.|| |     | |
   ../|' v . | .|||||/____|____\|||| /|. . | . ./
    |//\............/...........\........../../\\\

        A magnificant sight....!''',
        "choices": [
            {
                "scene": 0,
                "description": "Head back to the amazing scene"
            },
            {
                "scene": 2,
                "description": "Return to the village for BATTLE!"
            }
        ]
    },
    {
        "name": "some battle",
        "type": SCENE_TYPE_BATTLE,
        "description": """Arrive at the BATTLE SCENE!""",
        "boss": "Galgamore",
        "weapon": "throws skary snakes",
        "health": 5,
        "damage": 1,
        "choices": [
            {
                "scene": 0,
                "description": "Head back to the amazing scene"
            }
        ]
    }
]

global game
game = {
    "scene": None,
    "score": 0,
    "health": 100,
    "inventory": [
        INVENTORY_POTION,
        INVENTORY_SWORD
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


def print_inventory():
    print(banner('inventory: '))
    for i in game['inventory']:
        print('{0}: (id: {1})'.format(i['name'], i['id']))
        print("\tRemaining use: {0}".format(i['use']))
        print("\tDamage: {0}".format(i['damage']))
        print("\tHealth: {0}".format(i['health']))
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
    game['scene'] = scenes[scene]


def is_finished():
    """Detect if game is finished."""
    return game['finished']


def scene_is_battle(scene):
    """Detect if current scene is a battle."""
    return scene['type'] is SCENE_TYPE_BATTLE


def start_game():
    """Starts the game!"""
    new_or_existing = input(
        '''Would you like to start a new game (n) or open an existing (o)? ''')
    load_scene(0)

    if new_or_existing == 'o':
        load_game()

    print('Starting game from scene {0}'.format(game["scene"]["name"]))


def load_game():
    """Load a game from file."""
    file_name = input("Enter file to open: ")
    print("Reading game from file {0}".format(file_name))
    with open(file_name, 'r') as f:
        global game
        game = load(f)


def save_game():
    """Save a game from file."""
    file_name = input("Filename: ")
    print("Saving game to file {0}".format(file_name))
    with open(file_name, 'w') as f:
        dump(game, f)


def die():
    """You dead!"""
    game['health'] = 0
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

        answer = input('Select your move (by id): ')
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
    print(banner('\n\nYou make your way to {0} ...\n'.format(scene['name'])))

    if scene_is_battle(scene):
        load_scene(battle())
    else:
        print(scene['description'] + '\n\n')
        answered = False

        while answered is False:
            for option in scene['choices']:
                print('{0}: {1}'.format(
                    option['scene'], option['description']))
            answer = input('\nHow will you proceed? ')
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
    if is_finished is True:
        print("Game Over!")
        exit(0)

    display_scene()
