##Question ID: 883

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0
    last_arrival = -1

    for pos, sp in cars:
        arrival = (target - pos) / sp
        if arrival > last_arrival:
            fleets += 1
            last_arrival = arrival

    return fleets


## Structure
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    # Your code here

    pass