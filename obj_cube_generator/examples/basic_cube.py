from datetime import datetime
import sys
sys.path.insert(1, '..')
from CubesCodeGenerator import CubesCodeGenerator

def generateFileName():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return str(timestamp) + ".obj"

cubesCodeGenerator = CubesCodeGenerator()
file_name = generateFileName()
fr = open("../created_objs" + "/" + file_name, 'a')
fr.write(cubesCodeGenerator.generate("myCube"))
fr.close()

print("The file " + file_name + " has been generated.")
