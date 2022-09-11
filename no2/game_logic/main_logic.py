from designe import map as  map_import
from scene import scenemanager as scene_import
from entity import player as palyer

global main_player
main_player = palyer.player 

def main_logic():
    start()
    return

def start():
    #scene_import.load_scen(1)
    main_player.entity.initialize()
    main_player.entity.rotation = 0
    main_player.entity.position  = 0 
    main_player.entity.position = map_import.get_preSet_player_position()
    #main_player.entity.position[0] =  0 #x
    #main_player.entity.position[1] =  0 #y
    main_player.entity.destroy()
    return

def update_fixed():
    return
