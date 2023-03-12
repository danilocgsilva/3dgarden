def generate_positions() -> list:
    inertia = -0.4
    position = 30
    force = 0.0009
    positions = []
    for i in range(1000):
        inertia += force
        position = position + inertia
        positions.append(position)
    return positions
