##Question ID: 293

def generate_possible_next_moves(current_state):
    result = []
    for i in range(1, len(current_state)):
        if current_state[i] == '+' and current_state[i - 1] == '+':
            result.append(current_state[:i - 1] + '--' + current_state[i + 1:])
    return result

## Structure
def generate_possible_next_moves(current_state):
    # Your code here

    pass