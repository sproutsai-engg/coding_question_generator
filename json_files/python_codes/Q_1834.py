##Question ID: 1834

def minimum_teachings(n, languages, friendships):
    language_users = {}
    unconnected_users = set()

    for u, v in friendships:
        can_communicate = any(lang in languages[v-1] for lang in languages[u-1])
        if not can_communicate:
            unconnected_users.add(u)
            unconnected_users.add(v)

    res = len(unconnected_users)
    for i in range(1, n+1):
        cnt = sum(i not in languages[user-1] for user in unconnected_users)
        res = min(res, cnt)

    return res

## Structure
def minimum_teachings(n, languages, friendships):
    # Your code here

    pass