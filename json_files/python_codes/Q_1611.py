##Question ID: 1611

def get_folder_names(names):
    name_count = {}
    ans = []

    for name in names:
        if name not in name_count:
            ans.append(name)
            name_count[name] = 1
        else:
            k = name_count[name]
            new_name = f"{name}({k})"
            while new_name in name_count:
                k += 1
                new_name = f"{name}({k})"
            ans.append(new_name)
            name_count[new_name] = 1
            name_count[name] = k + 1

    return ans

## Structure
def get_folder_names(names):
    # Your code here

    pass