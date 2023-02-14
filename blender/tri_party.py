import bpy
from random import random
import math

def generateOneCube(cubeSize, ra1, ra2):
    
    bpy.ops.mesh.primitive_cube_add(
        enter_editmode=False, 
        align='WORLD', 
        location=(0, 0, 0), 
        scale=(cubeSize, cubeSize, cubeSize)
    )

    angle1deg = random() * ra1
    print('The angle 1 is ' + str(angle1deg))
    
    angle2deg = random() * ra2
    print('The angle 2 is ' + str(angle2deg))
    
    print('---')
    
    angle1 = math.radians(angle1deg)
    angle2 = math.radians(angle2deg)
    
    # angle 1 revision
    angle1 = angle1 * math.cos(angle2)

    # pass 1
    x = math.sin(angle1)
    y = math.cos(angle1)
    # pass 2
    y = y * math.cos(angle2)
    z = math.sin(angle2) * math.cos(angle1)

    bpy.ops.transform.translate(
        value=(x, y, z), 
        orient_axis_ortho='X', 
        orient_type='CURSOR', 
        orient_matrix=((1, 0, -0), (0, 1, 0), (0, 0, 1)), 
        orient_matrix_type='CURSOR', 
        constraint_axis=(True, False, False), 
        mirror=False, 
        use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', 
        proportional_size=1, 
        use_proportional_connected=False, 
        use_proportional_projected=False, 
        snap=False, 
        snap_elements={'INCREMENT'}, 
        use_snap_project=False, 
        snap_target='CLOSEST', 
        use_snap_self=False, 
        use_snap_edit=False, 
        use_snap_nonedit=False, 
        use_snap_selectable=False
    )

for i in range(1200):
    generateOneCube(0.01, 90, 90)