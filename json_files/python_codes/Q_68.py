##Question ID: 68

def fullJustify(words, maxWidth):
    result = []
    idx = 0
    while idx < len(words):
        total_chars = len(words[idx])
        last = idx + 1
        while last < len(words):
            if total_chars + 1 + len(words[last]) > maxWidth:
                break
            total_chars += 1 + len(words[last])
            last += 1
        gaps = last - idx - 1
        line = []
        if last == len(words) or gaps == 0:
            for i in range(idx, last):
                line.append(words[i])
                if i < last - 1:
                    line.append(" ")
            while sum(len(w) for w in line) < maxWidth:
                line.append(" ")
        else:
            even_spaces = (maxWidth - total_chars) // gaps
            extra_spaces = (maxWidth - total_chars) % gaps
            for i in range(idx, last):
                line.append(words[i])
                if i < last - 1:
                    line.append(" " * (even_spaces + (1 if i - idx < extra_spaces else 0)))
        idx = last
        result.append("".join(line))
    return result

## Structure
def fullJustify(words, maxWidth):
    # Your code here

    pass