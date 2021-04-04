import hashlib
class Codec:
    
    def __init__(self):
        self.cache = {}
        
    def get_md5_hash(self, s):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        return m.hexdigest()
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
        result = "www.mysite.com/"

        result += self.get_md5_hash(longUrl)
        
        self.cache[result] = longUrl
        return result     

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cache.get(shortUrl, None)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))