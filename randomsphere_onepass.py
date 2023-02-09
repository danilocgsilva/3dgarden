import sys
import bpy
from importlib import reload
sys.path.append("C:/Users/danil/pCloud/3d")
from random import random
import math
from datetime import datetime
import time

def createCube(size=2, location=(0 ,0, 0)):
    bpy.ops.mesh.primitive_cube_add(
        size=size, 
        enter_editmode=False, 
        align='WORLD', 
        location=location, 
        scale=(1, 1, 1)
    )

def getMilliseconds():
    return round(time.time() * 1000)

def getVector():
    x = random() * 2 - 1
    y = random() * 2 - 1
    z = random() * 2 - 1
    
    distance_from_center = math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
    
    vx = x * (1 / distance_from_center)
    vy = y * (1 / distance_from_center)
    vz = z * (1 / distance_from_center)

    return (vx, vy, vz)

starttime = getMilliseconds()
iteration = 1
for i in range(500):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    name = "cube-" + str(timestamp) + "-" + str(iteration)
    createCube(.02, getVector())
    bpy.context.selected_objects[0].name = name
    iteration += 1
endtime = getMilliseconds()

print("Took " + str(endtime - starttime) + " ms")
