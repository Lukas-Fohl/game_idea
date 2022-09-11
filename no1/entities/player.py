from collision import collision
from obj import obj 

game_obj = obj.game_object()
game_obj.position_x = 0
game_obj.position_y = 0
game_obj.height = 1
game_obj.lenght = 1
game_obj.state = "stand"

def input():
    #if input != 0
    #-->call movement or attack
    #else state = stand 
    return

def movement():
    collision.main_collide(game_obj,)   
    #state = move
    ##--> collide with object at coordinate
    return

def attack():
    #state = attack 
    #move box --> await 
    #check for collison
    collision.main_collide(game_obj,) 
    return