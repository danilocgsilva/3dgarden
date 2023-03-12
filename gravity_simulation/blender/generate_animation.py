import bpy
import sys
import os
sys.path.append("..")
from generate_positions import generate_positions

object_positions = generate_positions()

bpy.context.scene.frame_end = len(object_positions)

obj_to_animate = bpy.data.objects["Cube"]

keyframe = 0
for position in object_positions:
    bpy.context.scene.frame_set(keyframe)
    current_obj_position = obj_to_animate.location[2]
    next_obj_position = current_obj_position = position
    obj_to_animate.location[2] = next_obj_position
    obj_to_animate.keyframe_insert("location")
    keyframe += 1

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(os.getcwd(), "here.blend"))
