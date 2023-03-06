def calculate_decay_value(distance):
    return 1 / pow(distance, 2)

def motor(position, iteration):
    decay_value = calculate_decay_value(position)
    new_position = position - decay_value
    return position, new_position, decay_value

vector_speed = 0
position = 5
for i in range(100):
    old_position, position, decay_value = motor(position, i)
    print("old position: {0}, position: {1}, decay value: {2}".format(str(old_position), str(position), str(decay_value)))

