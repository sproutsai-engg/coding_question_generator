##Question ID: 985

def bag_of_tokens_score(tokens, power):
    tokens.sort()
    max_score = score = 0
    left, right = 0, len(tokens) - 1

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            left += 1
            score += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            right -= 1
            score -= 1
        else:
            break

    return max_score

## Structure
def bag_of_tokens_score(tokens, power):
    # Your code here

    pass