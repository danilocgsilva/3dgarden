def calculate_decay_value(distance):
    return 1 / pow(2, distance)

vector_speed = 0
position = 10
for i in range(1000):
    decay_value = calculate_decay_value(position)
    next_vector_speed = vector_speed * decay_value
    print(str(i) + ", 0")