##Question ID: 1312

def extract_artifacts(n, artifacts, dig):
    artifact_cells = {}
    artifact_count = {}

    for i, (r1, c1, r2, c2) in enumerate(artifacts):
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                cell = r * n + c
                if cell not in artifact_cells:
                    artifact_cells[cell] = set()
                artifact_cells[cell].add(i)
                artifact_count[i] = artifact_count.get(i, 0) + 1

    ans = 0
    for r, c in dig:
        cell = r * n + c
        if cell in artifact_cells:
            for artifact_id in artifact_cells[cell]:
                artifact_count[artifact_id] -= 1
                if artifact_count[artifact_id] == 0:
                    ans += 1
            del artifact_cells[cell]

    return ans

## Structure
def extract_artifacts(n, artifacts, dig):
    # Your code here

    pass