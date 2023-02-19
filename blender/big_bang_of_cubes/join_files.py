import os
import bpy

def isBlenderFile(file_name: str) -> bool:
    file_parts = file_name.split('.')
    file_last_part = file_parts[len(file_parts) - 1]
    if file_last_part == 'blend':
        return True
    return False

def join_here(file):
    full_file_path = os.path.join(os.getcwd(), 'created', file)
    with bpy.data.libraries.load(full_file_path) as (data_from, data_to):
        for object_to_append in data_from.objects:
            append_object(full_file_path, object_to_append)

def append_object(file_path, obj_name):
    bpy.ops.wm.append(
        filepath=os.path.join(file_path, "Object", obj_name),
        directory=os.path.join(file_path, "Object"),
        filename=obj_name
    )

for file in os.listdir('created'):
    if isBlenderFile(file):
        join_here(file)


