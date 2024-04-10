##Question ID: 140

def word_break(s, word_dict):
    def helper(s, dict, memo):
        if s in memo:
            return memo[s]

        res = []
        if s in dict:
            res.append(s)

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in dict:
                continue
            suffix = s[i:]
            temp = helper(suffix, dict, memo)
            for t in temp:
                res.append(prefix + " " + t)

        memo[s] = res
        return res

    word_set = set(word_dict)
    memo = {}
    return helper(s, word_set, memo)

## Structure
def word_break(s, word_dict):
    # Your code here

    pass