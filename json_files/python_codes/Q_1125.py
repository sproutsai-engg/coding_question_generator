##Question ID: 1125

from collections import defaultdict
from math import log2

def smallestSufficientTeam(req_skills, people):
    skill_to_id = {skill: idx for idx, skill in enumerate(req_skills)}

    n, m = len(people), len(req_skills)
    dp = [float("inf")] * (1 << m)
    pre = [0] * (1 << m)
    skill_set = [0] * (1 << m)

    dp[0] = 0

    for i, skills in enumerate(people):
        skill_mask = sum(1 << skill_to_id[skill] for skill in skills)
        for j in range((1 << m) - 1, -1, -1):
            if dp[j | skill_mask] > dp[j] + 1:
                dp[j | skill_mask] = dp[j] + 1
                pre[j | skill_mask] = j
                skill_set[j | skill_mask] = i

    res = []
    mask = (1 << m) - 1
    while mask:
        res.append(skill_set[mask])
        mask = pre[mask]

    return res


## Structure
from collections import defaultdict
    # Your code here

    pass