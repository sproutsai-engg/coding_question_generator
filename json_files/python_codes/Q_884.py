##Question ID: 884

def k_similarity(s1, s2):
    k = 0
    a, b = list(s1), list(s2)
    for i in range(len(a)):
        if a[i] != b[i]:
            for j in range(i + 1, len(b)):
                if a[i] == b[j] and a[j] != b[j]:
                    a[i], a[j] = a[j], a[i]
                    k += 1
                    break
    return k

## Structure
def k_similarity(s1, s2):
    # Your code here

    pass