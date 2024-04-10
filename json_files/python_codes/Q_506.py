##Question ID: 506

def find_relative_ranks(score):
    rank_sort = sorted(range(len(score)), key=lambda i: score[i], reverse=True)
    result = [0] * len(score)
    for i, rank in enumerate(rank_sort):
        result[rank] = i + 1
    return result


## Structure
def find_relative_ranks(score):
    # Your code here

    pass