import os
from datetime import datetime
import importlib.util
import sys
spec = importlib.util.spec_from_file_location(
    "big_bang", 
    os.path.join(
        os.getcwd(),
        "big_bang.py"
    )
)
big_bang = importlib.util.module_from_spec(spec)
sys.modules["big_bang"] = big_bang
spec.loader.exec_module(big_bang)
import bpy

amount_creation = 20

def clear_initial_objects():
    for obj in bpy.data.objects:
        print("Object to be deleted: " + obj.name)
        bpy.data.objects.remove(obj, do_unlink=True)

clear_initial_objects()

big_bang.generateBigbangExplosion(amount_creation)

file_name = os.path.join('created', 'bigbang-' + str(datetime.timestamp(datetime.now())) + '.blend')
file_path_full = os.path.join(os.getcwd(), file_name)

bpy.ops.wm.save_as_mainfile(filepath=file_path_full)
bpy.ops.wm.quit_blender()