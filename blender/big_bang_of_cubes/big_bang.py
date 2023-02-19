import bpy
from random import random
import math

creation_amount = 1000

def generateBigbangExplosion(creation_amount):

    def positeObject(obj, speed = 1.0):
        x = random() * 2 - 1
        y = random() * 2 - 1
        z = random() * 2 - 1
        
        distance_from_center = math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        
        obj.location.x += x * (1 / distance_from_center) * speed
        obj.location.y += y * (1 / distance_from_center) * speed
        obj.location.z += z * (1 / distance_from_center) * speed
            
    for i in range(creation_amount):
        bpy.ops.mesh.primitive_cube_add(size=0.05, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "obj" + str(i)

    mesh_objects = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            mesh_objects.append(obj)

    mesh_objects_count = len(mesh_objects)
    print("There are " + str(mesh_objects_count) + " mesh objects in the scene.")

    for obj in mesh_objects:
        bpy.context.scene.frame_set(1)
        obj.keyframe_insert("location")
        bpy.context.scene.frame_set(250)
        positeObject(obj, random())
        obj.keyframe_insert("location")
        object_fcurves = obj.animation_data.action.fcurves
        for fcurve in object_fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'LINEAR'
        #bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1) 
        mesh_objects_count -= 1
        print("Remaining: " + str(mesh_objects_count))

# Uncomment of you desire to execute the code without importing
# generateBigbangExplosion(creation_amount)
