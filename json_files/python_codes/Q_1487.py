##Question ID: 1487

def maxNumberOfFamilies(n, reservedSeats):
    rows = {}
    for seat in reservedSeats:
        rows[seat[0]] = rows.get(seat[0], 0) | (1 << (seat[1] - 1))
    
    max_groups = (n - len(rows)) * 2
    for row_mask in rows.values():
        seats = ~(row_mask | (row_mask >> 1) | (row_mask >> 2) | (row_mask >> 3)) & 0x3FF
        max_groups += (seats & (seats >> 1) & (seats >> 2) & (seats >> 3)) != 0
        
    return max_groups

## Structure
def maxNumberOfFamilies(n, reservedSeats):
    # Your code here

    pass