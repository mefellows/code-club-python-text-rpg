'''
The Scenes module contains all of the scene data for the game.
'''

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