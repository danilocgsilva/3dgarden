def calculate_decay_value(distance):
    return 1 / pow(distance, 2)

def motor(position, iteration):
    decay_value = calculate_decay_value(position)
    # next_vector_speed = 1 * decay_value
    position = position - decay_value
    print("iteration: " + str(iteration) + ", position: " + str(position) + ", decay value: " + str(decay_value))
    return position

# vector_speed = 0
# position = 10
# for i in range(3000):
#     position = motor(position, i)

motor(0.21481365662823804, 0)
