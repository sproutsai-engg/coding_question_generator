##Question ID: 165

def compare_version(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    
    while v1 or v2:
        num1 = int(v1.pop(0)) if v1 else 0
        num2 = int(v2.pop(0)) if v2 else 0
        
        if num1 < num2:
            return -1
        if num1 > num2:
            return 1
    return 0

## Structure
def compare_version(version1, version2):
    # Your code here

    pass