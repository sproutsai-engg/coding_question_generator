##Question ID: 751

def ipToCIDR(ip: str, n: int) -> List[str]:
    a, b, c, d = map(int, ip.split('.'))
    start = (a << 24) + (b << 16) + (c << 8) + d
    end = start + n - 1
    
    ans = []
    while start <= end:
        samePrefixBits = (~start & start).bit_length() - 1
        while ((end - start) >> samePrefixBits) < 1:
            samePrefixBits -= 1
        range = 1 << samePrefixBits
        ans.append(f"{start >> 24}.{(start >> 16) & 255}.{(start >> 8) & 255}.{start & 255}/{32 - samePrefixBits}")
        start += range
    
    return ans


## Structure
def ipToCIDR(ip: str, n: int) -> List[str]:
    # Your code here

    pass