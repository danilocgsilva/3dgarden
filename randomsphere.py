import sys
import bpy
from importlib import reload
sys.path.append("C:/Users/danil/pCloud/3d")
import criarcubo
reload(criarcubo)
from criarcubo import createCube
from random import random
import math
from datetime import datetime

def posite(name):
    
    x = random() * 2 - 1
    y = random() * 2 - 1
    z = random() * 2 - 1
    
    distance_from_center = math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
    
    vx = x * (1 / distance_from_center)
    vy = y * (1 / distance_from_center)
    vz = z * (1 / distance_from_center)
    
    bpy.ops.transform.translate(
        value=(vx, vy, vz), 
        orient_axis_ortho='X', 
        orient_type='GLOBAL', 
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
        orient_matrix_type='GLOBAL', 
        constraint_axis=(False, True, False), 
        mirror=False, 
        use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', 
        proportional_size=1, 
        use_proportional_connected=False, 
        use_proportional_projected=False, 
        snap=False, snap_elements={'INCREMENT'}, 
        use_snap_project=False, 
        snap_target='CLOSEST', 
        use_snap_self=False, 
        use_snap_edit=False, 
        use_snap_nonedit=False, 
        use_snap_selectable=False
    )
    
    bpy.context.selected_objects[0].name = name

iteration = 1
for i in range(1000):
    createCube(.02)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    name = "cube-" + str(timestamp) + "-" + str(iteration)
    posite(name)
    iteration += 1
