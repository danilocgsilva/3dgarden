import bpy

file_path = "C://aa//bb//cc//file" # your file path here
object_name = "object_name" # the scene object name

obj_to_animate = bpy.data.objects[object_name]

with open(file_path) as fp:
    keyframe = 0
    for line in fp:
        bpy.context.scene.frame_set(keyframe)
        current_obj_position = obj_to_animate.location[2]
        next_obj_position = current_obj_position = float(line)
        obj_to_animate.location[2] = next_obj_position
        print(str(next_obj_position))
        obj_to_animate.keyframe_insert("location")
        keyframe += 1

