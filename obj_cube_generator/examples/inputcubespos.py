import fileinput
from datetime import datetime
import sys
sys.path.insert(1, '..')
from CubesCodeGenerator import CubesCodeGenerator
import sys

def generateFileName():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return str(timestamp) + ".obj"

def get_tupple(raw_line):
    line_data_noend = raw_line.split("\n")
    line_data = line_data_noend[0].split(",")

    if len(line_data) == 3:
        return (
            float(line_data[0].strip().rstrip()),
            float(line_data[1].strip().rstrip()),
            float(line_data[2].strip().rstrip()),
            1.0
        )
    return (
        float(line_data[0].strip().rstrip()),
        float(line_data[1].strip().rstrip()),
        float(line_data[2].strip().rstrip()),
        float(line_data[3].strip().rstrip())
    )

cubesCodeGenerator = CubesCodeGenerator()
file_name = generateFileName()
fr = open(file_name, 'a')
iteration_offset = 1
for line in sys.stdin:
    position_data = get_tupple(line)
    cubeStringData = cubesCodeGenerator.generate(
        "cube-" + str(iteration_offset), 
        xoffset=position_data[0], 
        yoffset=position_data[1], 
        zoffset=position_data[2],
        size=position_data[3]
    )
    fr.write(cubeStringData)
    iteration_offset += 1
print('Created file ' + file_name)
