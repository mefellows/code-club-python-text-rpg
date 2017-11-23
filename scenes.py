'''
The Scenes module contains all of the scene data for the game.
'''

import inventory as i

# Scene types
SCENE_TYPE_SCENE = 0
SCENE_TYPE_BATTLE = 1
SCENE_TYPE_INVENTORY = 2

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
        "description": '''A magnificant sight....!''',
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
        "type": SCENE_TYPE_INVENTORY,
        "description": "",
        "item": i.INVENTORY_KEY,
        "choices": [
            {
                "scene": 0,
                "description": "Head to somewhere with your key.."
            }
        ]
    }
]
