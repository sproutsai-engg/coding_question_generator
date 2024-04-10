##Question ID: 733

def floodFill(image, sr, sc, newColor):
    startColor = image[sr][sc]
    def fill(sr, sc):
        if not (0 <= sr < len(image)) or not (0 <= sc < len(image[0])) or image[sr][sc] != startColor or image[sr][sc] == newColor: 
            return
        image[sr][sc] = newColor
        fill(sr - 1, sc)
        fill(sr + 1, sc)
        fill(sr, sc - 1)
        fill(sr, sc + 1)
    
    fill(sr, sc)
    return image


## Structure
def floodFill(image, sr, sc, newColor):
    # Your code here

    pass