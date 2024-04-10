##Question ID: 1027

def sumEvenAfterQueries(nums, queries):
    answer = []
    even_sum = sum(num for num in nums if num % 2 == 0)

    for value, index in queries:
        if nums[index] % 2 == 0:
            even_sum -= nums[index]
        nums[index] += value
        if nums[index] % 2 == 0:
            even_sum += nums[index]
        answer.append(even_sum)

    return answer


## Structure
def sumEvenAfterQueries(nums, queries):
    # Your code here

    pass