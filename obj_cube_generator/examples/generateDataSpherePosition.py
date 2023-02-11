from random import random
import math

range_length = 10000

for i in range(range_length):
    x = random() * 2 - 1
    y = random() * 2 - 1
    z = random() * 2 - 1

    distance_from_center = math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))

    vx = x * (1 / distance_from_center)
    vy = y * (1 / distance_from_center)
    vz = z * (1 / distance_from_center)

    print("{0},{1},{2},{3}".format(vx, vy, vz, 0.01))
