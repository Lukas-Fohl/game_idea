from enum import Enum

class block(Enum):
    air = 0
    normal = 1

class entity():
    image = ""
    position = [0,0]  #in pixels
    function = [None] #include functions to have from smol_game/entity.py/function
    def __init__(self):
        return

