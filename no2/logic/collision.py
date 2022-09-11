from entity import enitiy_main as entity_main_import

def normal_collision(entity_1: entity_main_import,entity_2: entity_main_import):
    #print(entity_1.rotation)   --> works
    return False

def multi_collision(entity_list:  entity_main_import = {}):
    #print(entity_list[len(entity_list)-1].rotation) --> works
    return False

def all_check_collision():
    return False

"""
example 
ent_listing = [main_logic_import.main_player.entity, main_logic_import.main_player.entity]
collision_import.multi_collision(ent_listing)
"""