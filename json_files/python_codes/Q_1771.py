##Question ID: 1771

def maxProfit(inventory, orders):
    mod = 10**9 + 7
    inventory.sort(reverse=True)
    inventory.append(0)
    n, ans, count = len(inventory), 0, 1
    for i in range(n - 1):
        diff = inventory[i] - inventory[i + 1]
        if count * diff < orders:
            orders -= count * diff
            ans = (ans + (((inventory[i] + inventory[i + 1] + 1) * diff) // 2) % mod * count) % mod
        else:
            q, r = divmod(orders, count)
            ans = (ans + (((inventory[i] + inventory[i] - q + 1) * q) // 2) % mod * count) % mod
            ans = (ans + r * (inventory[i] - q)) % mod
            break
        count += 1
    return ans

## Structure
def maxProfit(inventory, orders):
    # Your code here

    pass