from scene import scenemanager as sceneManger_import
import platform
import json
import os

map_2d   =[[],[]]
append_str = "/"
if platform.system() == 'Windows':
    append_str = "\\"
map_path =  os.path.dirname(os.path.abspath(__file__)) +append_str+"main.json"
map_data = {}

def translate_map(scene_in,map_in):
    with open(map_path,"r") as json_file:
        map_data = json.load(json_file)
        map_2d = map_data[scene_in][map_in]
    return map_2d

def get_current_map():
    with open(map_path,"r") as json_file:
        return json.load(json_file)["current"]

def get_preSet_player_position():
    map_2d = translate_map(sceneManger_import.scene_now,sceneManger_import.map_now)
    x_counter = 0
    y_counter = 0
    for y in map_2d:
        for x in y:
            if(x== 's'):
                return [x_counter,y_counter]
            x_counter += 1
        x_counter = 0
        y_counter +=1

def get_current_player_position():
    map_2d = get_current_map()
    x_counter = 0
    y_counter = 0
    for y in map_2d:
        for x in y:
            if(x== 's'):
                return [x_counter,y_counter]
            x_counter += 1
        x_counter = 0
        y_counter +=1