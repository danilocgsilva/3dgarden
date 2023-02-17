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

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.context.scene.frame_set(1)
        obj.keyframe_insert("location")
        bpy.context.scene.frame_set(250)
        positeObject(obj)
        obj.keyframe_insert("location")
        
        action = obj.animation_data.action
        fcurves = [fc for fc in action.fcurves]
        for fcurve in fcurves:
            for kfp in fcurve.keyframe_points:
                if kfp.co.x == time:
                    print("scale.%s easing set to EASE_IN at frame %d" % ("xyz"[fcurve.array_index], time))
                    kfp.easing = 'EASE_IN' #  auto 