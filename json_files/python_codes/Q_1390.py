##Question ID: 1390

def sum_of_four_divisors(nums):
    total_sum = 0
    for num in nums:
        count = 0
        div_sum = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                count += 1 if i * i == num else 2
                div_sum += i + (num // i)
                if count > 4:
                    break
            i += 1
        if count == 4:
            total_sum += div_sum
    return total_sum

## Structure
def sum_of_four_divisors(nums):
    # Your code here

    pass