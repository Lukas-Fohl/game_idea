from util import util as util

global width_
global height_
height_ = 18
width_ = 32
global real_heigth
global real_width
real_heigth = 720
real_width  = 1280
global display_grid
display_grid = [[util.block.normal for y in range(height_)] for x in range(width_)]
entity_grid = [util.entity for y in range(1)]

class map:
    def __init__(self):
        entity_grid[0].position[0] = 5
        entity_grid[0].position[1] = 5
        entity_grid[0].image       = "smol.png"
        display_grid[width_-1][height_-1] = util.block.air
        for y in range(height_):
            for x in range(width_):
                if y > 12:
                   display_grid[x][y] = util.block.normal 
                else:
                    display_grid[x][y] = util.block.air

