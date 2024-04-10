##Question ID: 1618

def max_font_size(text: str, w: int, h: int, fonts: List[int], font_info) -> int:
    left, right, ans = 0, len(fonts) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        font_size = fonts[mid]
        width, height = sum(font_info.getWidth(font_size, ch) for ch in text), font_info.getHeight(font_size)
        if width <= w and height <= h:
            ans = font_size
            left = mid + 1
        else:
            right = mid - 1
    return ans

## Structure
def max_font_size(text: str, w: int, h: int, fonts: List[int], font_info) -> int:
    # Your code here

    pass