##Question ID: 1233

from typing import List

def removeSubfolders(folder: List[str]) -> List[str]:
    result = []
    folder.sort()
    prefix = "/"
    
    for path in folder:
        if not path.startswith(prefix):
            result.append(path)
            prefix = path + "/"
    return result

## Structure
from typing import List
    # Your code here

    pass