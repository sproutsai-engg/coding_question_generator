##Question ID: 681

def nextClosestTime(time: str) -> str:
    digits = time[:2] + time[3:]
    next_time = time
    elapsed = float('inf')

    for a in digits:
        for b in digits:
            for c in digits:
                for d in digits:
                    candidate_time = f"{a}{b}:{c}{d}"
                    cand_elapsed = (int(candidate_time[:2]) * 60 + int(candidate_time[3:]) -
                                    int(time[:2]) * 60 - int(time[3:]) + 1440) % 1440
                    if 0 < cand_elapsed < elapsed:
                        elapsed = cand_elapsed
                        next_time = candidate_time

    return next_time

## Structure
def nextClosestTime(time: str) -> str:
    # Your code here

    pass