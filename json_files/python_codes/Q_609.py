##Question ID: 609

from collections import defaultdict

def find_duplicate(paths):
    content_map = defaultdict(list)
    for path in paths:
        parts = path.split()
        directory = parts[0]
        for file in parts[1:]:
            start = file.index('(')
            end = file.index(')')
            content = file[start + 1:end]
            file_path = directory + '/' + file[:start]
            content_map[content].append(file_path)

    result = [file_paths for file_paths in content_map.values() if len(file_paths) > 1]
    return result

## Structure
from collections import defaultdict
    # Your code here

    pass