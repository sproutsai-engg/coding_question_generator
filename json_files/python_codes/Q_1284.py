##Question ID: 1284

def sum_of_divisors_with_four_divisors(nums):
    total_sum = 0

    for num in nums:
        div_count = 0
        div_sum = 0

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                div_sum += i
                div_count += 1

                if num // i != i:
                    div_sum += num // i
                    div_count += 1

            if div_count > 4:
                break

        if div_count == 4:
            total_sum += div_sum

    return total_sum

## Structure
def sum_of_divisors_with_four_divisors(nums):
    # Your code here

    pass