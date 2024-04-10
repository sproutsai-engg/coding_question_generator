##Question ID: 1220

from typing import List

def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
    skill_to_int = {s: i for i, s in enumerate(req_skills)}
    people_skills = [sum(1 << skill_to_int[skill] for skill in person) for person in people]
        
    n = len(req_skills)
    INF = 64
    dp = [INF] * (1 << n)
    dp[0] = 0
    parent = [None] * (1 << n)
        
    for i, person_skills in enumerate(people_skills):
        for completed_skills in range((1 << n) - 1, -1, -1):
            with_person_skills = completed_skills | person_skills
            if dp[with_person_skills] > dp[completed_skills] + 1:
                dp[with_person_skills] = dp[completed_skills] + 1
                parent[with_person_skills] = completed_skills
                
    ans = [0] * dp[-1]
    cur = (1 << n) - 1
    t = dp[-1] - 1
        
    for i in range(len(people) - 1, -1, -1):
        old = parent[cur]
        diff = cur ^ old
        is_essential = (people_skills[i] & diff) > 0
        if is_essential:
            ans[t] = i
            t -= 1
        cur = old
    return ans

## Structure
from typing import List
    # Your code here

    pass