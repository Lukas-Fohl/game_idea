from time import sleep
import time
import pygame
import random
from display import display as display_import
from logic import logic as logic_import
from util import util as util

background_colour = (255,255,255)
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('smol')
screen.fill(background_colour)
pygame.display.flip()

global current_milis
global last_milis

global air_img
air_img  = pygame.image.load('assests\\air.png')
global smol_img
smol_img = pygame.image.load('assests\\smol.png')

global gamedis
gamedis = pygame.display.set_mode((width, height))

global new_map

def setframe():
    global new_map
    new_map = display_import.map() 
    running = True
    while running:
        #Frame --> works wih delta time
        logic_import.main_logic()
        displaying()
        display_entity()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return

def display_entity():
    #look for all entitys that have to be renderd and do it
    for ent in range(len(display_import.entity_grid)): 
        gamedis.blit(pygame.image.load("assests\\"+str(display_import.entity_grid[ent].image)),(display_import.entity_grid[ent].position[0],display_import.entity_grid[ent].position[1]))
    return

def displaying():
    last_milis = int(round(time.time()*1000))
    for y in range(display_import.height_):
        for x in range(display_import.width_):
            gamedis.blit(block_type(display_import.display_grid[x][y]),(40*x,40*y))
    current_milis = int(round(time.time()*1000))
    dif = (int(current_milis)-int(last_milis))
    if dif < 16:
        #delta time
        sleep((16-dif)/1000)
    else:
        print("we are not fast enough")
    return

def block_type(input: util.block):
    match(input):
        case util.block.air:
            return air_img
        case _:
            return smol_img

if __name__ == "__main__":
    setframe()
