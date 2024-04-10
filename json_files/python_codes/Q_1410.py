##Question ID: 1410

def entity_parser(text: str) -> str:
    entities = {
        "&quot;": "\"",
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;": "/",
    }
    
    result = []
    current_entity = []
    in_entity = False
    
    for c in text:
        if in_entity:
            current_entity.append(c)
            if c == ';':
                entity = ''.join(current_entity)
                if entity in entities:
                    result.append(entities[entity])
                else:
                    result.extend(current_entity)
                in_entity = False
                current_entity.clear()
        else:
            if c == '&':
                in_entity = True
                current_entity.append(c)
            else:
                result.append(c)

    return ''.join(result)

## Structure
def entity_parser(text: str) -> str:
    # Your code here

    pass