scene = ["scene_1","scene_1","scene_1"]
scene_now = "scene_1"
map_now = "map_1"

def load_scen(index):
    global scene_now
    scene_now = scene[index] 
    change()
    return

def change():
    return