##Question ID: 871

def can_visit_all_rooms(rooms):
    visited = set()
    stack = [0]

    while stack:
        current_room = stack.pop()

        visited.add(current_room)

        for key in rooms[current_room]:
            if key not in visited:
                stack.append(key)

    return len(visited) == len(rooms)

## Structure
def can_visit_all_rooms(rooms):
    # Your code here

    pass