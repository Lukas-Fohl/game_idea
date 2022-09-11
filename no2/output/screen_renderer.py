from output import output as output_import
import math as math_import
import pygame
import json
import os
import platform

path_contain = os.path.dirname(os.path.abspath(__file__)) 

game_size = [0,0]
view_in = []
view_out = []

def renderer(view_from_ray_cast: int = []):
    #terminal_debug(view_in)
    global view_in
    view_in = view_from_ray_cast
    fish_eye_corg()
    get_game_size()
    init_view()
    pygame.init()
    DISPLAY=pygame.display.set_mode((4*game_size[0],4*game_size[1]),0,32)
    BLUE=(10,100,10)
    DISPLAY.fill((132, 236, 250))
    for y in range(len(view_out)):
        #mirrored final view
        pygame.draw.rect(DISPLAY,BLUE,(((game_size[0]*4)/len(view_out))*y,((game_size[1]*4)/2-(game_size[1]/2))-view_out[y]*10,((game_size[0]*4)/len(view_out))+2,view_out[y]*30))    
    #                               pos pos size size
    #pygame.draw.rect(DISPLAY,BLUE,(200,150,100,100))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
    return

def fish_eye_corg():
    global view_in
    return

def get_game_size():
    config_path = " "
    split_str = "/"
    if platform.system() == 'Windows':
        split_str = "\\"
    for x in range(len(path_contain.split(split_str))-1):
        config_path += path_contain.split(split_str)[x] + split_str
    config_path += "config.json"
    config_path = config_path[1:]

    with open(config_path,"r") as json_file:
        data_in = json.load(json_file)
        game_size[0] = data_in['game_size'][0]
        game_size[1] = data_in['game_size'][1]
    return

def  init_view():
    for x in range(len(view_in)):
        new_angle = x*(output_import.degrees_per_ray)
        view_out.append(view_in[x] * math_import.cos(deg_2_rad(output_import.view_offset + new_angle)))
    return	

def deg_2_rad(deg:float):
    return (deg)*(math_import.pi/180)

def terminal_debug():
    global view_in
    for x in range(len(view_in)):
        print(view_in[x] * math_import.cos())
    return