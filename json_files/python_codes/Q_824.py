##Question ID: 824

def number_of_lines(widths, s):
    lines = 1
    current_pixel = 0
    for c in s:
        letter_pixels = widths[ord(c) - ord('a')]
        if current_pixel + letter_pixels > 100:
            lines += 1
            current_pixel = 0
        current_pixel += letter_pixels
    return [lines, current_pixel]


## Structure
def number_of_lines(widths, s):
    # Your code here

    pass