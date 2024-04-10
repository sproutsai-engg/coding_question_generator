##Question ID: 829

from collections import defaultdict

def subdomainVisits(cpdomains):
    counts = defaultdict(int)
    result = []

    for cpdomain in cpdomains:
        count, domain = cpdomain.split()
        count = int(count)

        for i in range(len(domain)):
            if domain[i] == '.':
                counts[domain[i + 1:]] += count
        counts[domain] += count

    for sub, cnt in counts.items():
        result.append(f"{cnt} {sub}")
        
    return result


## Structure
from collections import defaultdict
    # Your code here

    pass