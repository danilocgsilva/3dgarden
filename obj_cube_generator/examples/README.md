# Examples for `CubesCodeGenerator.py`

Follows the explanation for files in this section.

### **`basic_cube.py`**

Uses the `CubesCodeGenerator` class and creates an .obj file with just one cube just for the demonstration sake.


### **`generateDataSpherePosition.py`**

Another piece of code decoupled from Blender. This is the *vector position calculation* almost isolated from everything else. It is just the vector generation for a single object, that is, a position from something distanct in one unit from the center, pointed to a completely random direction, done 10.000 times. In addition for all three axis values, an additional value of 0.01. This is throwed to the standart output, so easily can be used to be consumed by other piece of software.

### **`inputcubespos.py`**

This is cool one. This script is designed to read the data from a text file from standard input, iterates for each file line, uses the `CubeCodeGenerator.py` to create an .obj chunk of cube representing a cube based on each line file, and them creates an .obj file containing all cubes.

### **`10000cubes.data`**

This is an example of the `generateDataSpherePosition.py` result to be used on the go. You can use the `generateDataSpherePosition.py` script to generate any number of cubes at once just changing the `range_length` variable, but `10000cubes.data` is already a result for 10.000 positions forming a sphere to be used in `inputcubespos.py`.

### **`1676129751.722362.obj`**

An example of `inputcubespos.py` usage, consuming `10000cubes.data` file. Just import it any 3d suite software that understands the .obj format.
