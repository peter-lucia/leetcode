class Codec:
    def __init__(self):
        self.lookup = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        alpha_numeric = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
        alpha_numeric_length = len(alpha_numeric)
        shortened = ""
        c = len(self.lookup)
        while c > 0:
            shortened += alpha_numeric[self.count % alpha_numeric_length]
            c -= 1
        self.lookup[shortened] = longUrl
        return shortened
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.lookup.get(shortUrl, None)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))