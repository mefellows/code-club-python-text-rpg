#!/usr/bin/env python

from pyfiglet import figlet_format
from pickle import load, dump
from enum import Enum

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
print(figlet_format(title, font='slant'))
print banner('by: ' + authors)
print('')

# Game Constants
INFINITY = float("inf")

# Inventory
INVENTORY_POTION = {
  "damage": 0,
  "health": 25,
  "use": 5
}

INVENTORY_SWORD = {
  "damage": 25,
  "healh": 0,
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
                      when the scene shows up, and may contain ASCII pictures!""",
    "choices": [
      {
        "scene": 1,
        "description": "Head North to the castle"
      },
      {
        "scene": 2,
        "description": "Return to the village"
      }
    ]
  },
  {
    "name": "some battle",
    "type": SCENE_TYPE_BATTLE,
    "description": """some amazing description of this scene, this will be elaborated on
                      when the scene shows up, and may contain ASCII pictures!""",
    "boss": "Galgamore",
    "health": 5,
    "damage": 1,
    "choices": [
      {
        "scene": 1,
        "description": "Head North to the castle"
      },
      {
        "scene": 2,
        "description": "Return to the village"
      }
    ]
  }
]

game = {
    "scene": 0,
    "score": 0,
    "health": 100,
    "inventory": [
      INVENTORY_POTION 
    ],
    "finished": False,
}

def load_scene(scene):
    """Loads a scene by id into the current game scene."""
    game['scene'] = scenes[scene]

def start_game():
    """Starts the game!"""
    new_or_existing = raw_input('''Would you like to start a new game (n) or open an existing (o)? ''')
    load_scene(0)

    if new_or_existing == 'o':
      load_game()

    print 'Starting game from scene {0}'.format(game["scene"]["name"])

def load_game():
    """Load a game from file."""
    file_name = raw_input("Enter file to open: ")
    print "Reading game from file {0}".format(file_name)
    game = load(file_name)
    print game

def save_game():
    """Save a game from file."""
    file_name = raw_input("Filename: ")
    print "Saving game to file {0}".format(file_name)
    dump(game, file_name)

def scene_is_battle():
    """Detect if current scene is a battle."""
  

def battle():
    """Battle!"""
    scene = game['scene']
    print "You are now about to battle {0}".format(scene['boss'])

def help():
    """Print help!"""
    print """
      inventory: prints current inventory
      game: prints current game status
      quit: save and quits
    """

def print_inventory():
  print 'inventory: '

def print_game_status():
  print 'game status: '

def nothing():
  """do nothing"""

def do_menu_action(action):
    """Execute menu action!"""
    return {
      'inventory': print_inventory,
      'game': print_game_status,
      'quit': save_game,
      }.get(action, nothing)
      


def display_scene():
    """Display a scene."""
    scene = game['scene']

    # Is the scene a battle?
    if scene_is_battle():
      battle()
    else:
      print scene['description'] + '\n\n'
      
      answered = False

      while answered is False:
        for option in scene['choices']:
          print '{0}: {1}'.format(option['scene'], option['description'])
        answer = raw_input('How will you proceed? \n')
        try:
          if int(answer) in map((lambda x: x['scene']), scene['choices']):
            answered = True
          else:
            print "Invalid answer. "
        except ValueError:
          do_menu_action(answer)()

    

def is_finished():
    """Detect if game is finished."""

# Game Loop!

# 1. New Game or load existing?
start_game()

# 2. Display scene
while True:
    if is_finished is True:
      print "Game Over!"
      exit(0)

    display_scene()
