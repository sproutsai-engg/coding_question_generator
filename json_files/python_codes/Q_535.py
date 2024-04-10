##Question ID: 535

import random
import string

class Solution:
    def __init__(self):
        self.url_map = {}
        self.alphabet = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        key = ''.join(random.choices(self.alphabet, k=6))

        while key in self.url_map:
            key = ''.join(random.choices(self.alphabet, k=6))

        self.url_map[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl[-6:]]

## Structure
import random
    # Your code here

    pass