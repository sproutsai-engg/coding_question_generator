##Question ID: 735

def asteroidCollision(asteroids):
    s = []
    for num in asteroids:
        if num > 0 or not s or s[-1] < 0:
            s.append(num)
        elif s[-1] <= -num:
            if s[-1] < -num:
                s.pop()
                s.append(num)
            else:
                s.pop()
    return s


## Structure
def asteroidCollision(asteroids):
    # Your code here

    pass