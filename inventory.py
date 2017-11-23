'''
The Inventory module contains all of the tyes of inventory that can
be used throughout the game.
'''

INFINITY = float("inf")

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