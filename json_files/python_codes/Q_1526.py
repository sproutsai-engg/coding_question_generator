##Question ID: 1526

def entityParser(text: str) -> str:
    entities = {
        "&quot;": '\"',
        "&apos;": '\'',
        "&amp;": '&',
        "&gt;": '>',
        "&lt;": '<',
        "&frasl;": '/'
    }

    result, i = [], 0
    while i < len(text):
        if text[i] == '&':
            temp = ''
            for j in range(i, min(i+7, len(text))):
                temp += text[j]
                if temp in entities:
                    result.append(entities[temp])
                    i = j
                    break
            else:
                result.append(text[i])
        else:
            result.append(text[i])
        i += 1
    return ''.join(result)


## Structure
def entityParser(text: str) -> str:
    # Your code here

    pass