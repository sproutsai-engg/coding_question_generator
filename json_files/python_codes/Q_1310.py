##Question ID: 1310

def water_plants(plants, capacity):
    steps = 0
    water_left = 0

    for i, plant in enumerate(plants):
        if water_left < plant:
            steps += 2 * i + 1  # Refill the watering can
            water_left = capacity
        water_left -= plant
        steps += 1  # Move to the next plant

    return steps


## Structure
def water_plants(plants, capacity):
    # Your code here

    pass