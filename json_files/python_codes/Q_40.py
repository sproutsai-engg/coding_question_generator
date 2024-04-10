##Question ID: 40

def combinationSum2(candidates, target):
    def combine(candidates, target, start, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            combine(candidates, target - candidates[i], i+1, path + [candidates[i]], res)

    candidates.sort()
    res = []
    combine(candidates, target, 0, [], res)
    return res


## Structure
def combinationSum2(candidates, target):
    # Your code here

    pass