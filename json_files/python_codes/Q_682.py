##Question ID: 682

def calPoints(ops):
    record = []
    for op in ops:
        if op == '+':
            record.append(record[-1] + record[-2])
        elif op == 'D':
            record.append(record[-1] * 2)
        elif op == 'C':
            record.pop()
        else:
            record.append(int(op))
    return sum(record)


## Structure
def calPoints(ops):
    # Your code here

    pass