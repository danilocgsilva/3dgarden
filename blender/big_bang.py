import bpy
from random import random
import math

def positeObject(obj):
    x = random() * 2 - 1
    y = random() * 2 - 1
    z = random() * 2 - 1
    
    distance_from_center = math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
    
    obj.location.x = x * (1 / distance_from_center)
    obj.location.y = y * (1 / distance_from_center)
    obj.location.z = z * (1 / distance_from_center)
    
        
# for i in range(250):
#     bpy.ops.mesh.primitive_cube_add(size=0.05, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
#     bpy.context.object.name = "obj" + str(i)

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.context.scene.frame_set(1)
        obj.keyframe_insert("location")
        bpy.context.scene.frame_set(250)
        positeObject(obj)
        obj.keyframe_insert("location")
        object_fcurves = obj.animation_data.action.fcurves
        for fcurve in object_fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'LINEAR'