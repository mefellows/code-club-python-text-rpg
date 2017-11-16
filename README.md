# Realm: Text-based RPG framework

Text-based RPG game mini-framework


## Game Design \ Rules

* Game
    * Variables
        * Character
            * Health: int
            * Inventory: [array of strings]
        * Current scene (save): map
            * scene: int
            * health: int
            * inventory: [string]
        * Scenes - [array of Scene]
            * Contains all scene information for the entire game (essentially the game map)
    * Functions
        * Navigate
            * Responsible for navigating between scenes/battles
        * Fight
            * Takes the current health, inventory + the battle
            * Knows how to do “play by play” moves
            * Once a fight starts, there is no going back
            * Cannot save mid-fight?
* Scene
    * Description text
    * 2 choices
        * Each choice takes you to a scene OR a battle
    * Contains the rules/logic to move between other scenes or battles
* Battle
    * Another type of scene, with specific moves
    * Actions available
        * Leave battle?
        * Fight
    * Contains the options available after a successful battle
* Boss
    * Health
    * Damage associated with each attack
* Character
    * Health: int
    * Inventory: [array of strings]
* Weapon
    * Damage associated with each attack
