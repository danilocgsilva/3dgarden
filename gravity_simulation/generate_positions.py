inertia = -0.4
position = 0
force = 0.001

for i in range(1000):
    inertia += force
    position = position + inertia
    print(str(position))
