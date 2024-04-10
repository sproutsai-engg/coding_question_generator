##Question ID: 1899

def count_matches(items, rule_key, rule_value):
    rule = {"type": 0, "color": 1, "name": 2}
    count = 0

    for item in items:
        if item[rule[rule_key]] == rule_value:
            count += 1

    return count

## Structure
def count_matches(items, rule_key, rule_value):
    # Your code here

    pass