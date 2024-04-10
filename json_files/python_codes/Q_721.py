##Question ID: 721

from collections import defaultdict

def accountsMerge(accounts):
    def dfs(id, visited, merged_emails):
        if id in visited:
            return
        visited.add(id)
        for email in accounts[id][1:]:
            merged_emails.add(email)
            dfs(email_to_id[email], visited, merged_emails)

    email_to_id = {}
    for i, account in enumerate(accounts):
        for email in account[1:]:
            email_to_id[email] = i

    result = []
    visited = set()
    for i, account in enumerate(accounts):
        if i not in visited:
            merged_emails = set()
            dfs(i, visited, merged_emails)
            result.append([account[0]] + sorted(merged_emails))
    return result


## Structure
from collections import defaultdict
    # Your code here

    pass