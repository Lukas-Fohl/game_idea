from designe import map as map_import
from output import ray_cast as ray_cast_import
from scene import scenemanager as scene_manager_import
from output import screen_renderer as screen_renderer_import
import time as time_import
import math as math_import
import platform
import json
import os 

config_path = ""
path_contain = os.path.dirname(os.path.abspath(__file__)) 

game_map_now = [[],[]]
game_map = [[],[]]
scene_chosen = ""
map_chosen = ""
cam_eq_player = True
frame_rate = 30
ray_amount = 100
fov = 90
render_distacne = 10
view = []
view_offset = 0
degrees_per_ray = 0

def set_up(custom):
    get_json_config()
    values_set()
    if (custom == False):
        initi()
    global game_map_now
    game_map_now = map_import.translate_map(scene_chosen,map_chosen)
    return

def output_manager(custom):
    degrees_per_ray = fov/ray_amount
    view_offset = (180-fov)/2 # 35°
    #view_offset = 0
    for turning in range(ray_amount):
        if (turning*degrees_per_ray) == 0 or (turning*degrees_per_ray) % 15 == 0:
            turning += 0.1
        ray_cast_import.raycasting(render_distacne,view_offset + (turning*degrees_per_ray),map_import.get_current_map())
    screen_renderer_import.renderer(ray_cast_import.final_view)
    print("[✅] \t\t\t frame")
    exit()
    return

def initi():
    global scene_chosen
    global map_chosen
    global cam_eq_player
    scene_chosen = scene_manager_import.scene_now
    map_chosen = scene_manager_import.map_now
    cam_eq_player = True
    return

def get_json_config():
    global config_path 
    config_path = " "
    split_str = "/"
    if platform.system() == 'Windows':
        split_str = "\\"
    for x in range(len(path_contain.split(split_str))-1):
        config_path += path_contain.split(split_str)[x] + split_str
    config_path += "config.json"
    config_path = config_path[1:]
    return

def values_set():
    with open(config_path,"r") as json_file:
        global frame_rate
        global ray_amount
        global fov
        global render_distacne
        data_in = json.load(json_file)
        frame_rate = data_in['frame_rate']
        ray_amount = data_in['ray_cast_amount']
        fov = data_in['fov']
        render_distacne = data_in['render_distacne']
    return