import os
import bpy

def isBlenderFile(file_name: str) -> bool:
    file_parts = file_name.split('.')
    file_last_part = file_parts[len(file_parts) - 1]
    if file_last_part == 'blend':
        return True
    return False

def join_from_file(file):
    print('Joining file: ' + file)
    full_file_path = os.path.join(os.getcwd(), 'created', file)
    with bpy.data.libraries.load(full_file_path) as (data_from, data_to):
        append_object(full_file_path, data_from.objects, file)

def append_object(file_path, objects, file_name):

    objects_to_append = []
    for object in objects:
        dict_data_file = {'name': object}
        objects_to_append.append(dict_data_file)

    print('The file ' + file_name + ' have ' + str(len(objects_to_append)) + ' objects to be appended.')
    bpy.ops.wm.append(
        filepath=os.path.join(file_path, "Object", file_name),
        directory=os.path.join(file_path, "Object"),
        files=objects_to_append
    )

files_to_join = []
for file in os.listdir('created'):
    if isBlenderFile(file):
        files_to_join.append(file)

print('There are ' + str(len(files_to_join)) + ' to be joined.')
print(files_to_join)
for file_joining in files_to_join:
    join_from_file(file)
