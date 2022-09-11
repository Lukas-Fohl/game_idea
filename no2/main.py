from game_logic import main_logic as main_logic_import
from designe import map as map_import
from output import output as output_import
from logic import collision as collision_import
import sys

#global map_now_in_use
#global scene_now_in_use

def main():
    sys.setrecursionlimit(6**10)
    main_logic_import.main_logic()
    output_import.set_up(False)
    print("[✅] \t\t\t setup")
    looping()
    return

def looping():
    #tick: --> delta time
    output_import.output_manager(False)
    main_logic_import.update_fixed()
    looping()
    return

if __name__ == "__main__":
    main()

"""
what has to be done:
    import logic for own game logic 
    call output --> False:
        no custom values 
    call output --> True:
        custom values --> set own values after 

////////////////////////
this file is used to change the behavior of the rendering, logic and the over all behavior of the programm not for the logic of the game it self
////////////////////////
"""