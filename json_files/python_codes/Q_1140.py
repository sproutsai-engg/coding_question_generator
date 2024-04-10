##Question ID: 1140

from heapq import heappush, heappop

def rearrange_barcodes(barcodes):
    count = {}
    for barcode in barcodes:
        if barcode not in count:
            count[barcode] = 0
        count[barcode] += 1

    pq = []
    for key, value in count.items():
        heappush(pq, (-value, key))

    idx = 0
    while pq:
        curr = heappop(pq)
        while curr[0] < 0:
            barcodes[idx] = curr[1]
            curr = (curr[0] + 1, curr[1])
            idx += 2
            if idx >= len(barcodes):
                idx = 1
    return barcodes

## Structure
from heapq import heappush, heappop
    # Your code here

    pass