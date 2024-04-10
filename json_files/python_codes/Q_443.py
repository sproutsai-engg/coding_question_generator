##Question ID: 443

def compress(chars):
    index, i = 0, 0
    
    while i < len(chars):
        count = 1
        while i + count < len(chars) and chars[i] == chars[i + count]:
            count += 1
            
        chars[index] = chars[i]
        index += 1
        
        if count > 1:
            count_str = str(count)
            for c in count_str:
                chars[index] = c
                index += 1
                
        i += count
        
    return index

## Structure
def compress(chars):
    # Your code here

    pass