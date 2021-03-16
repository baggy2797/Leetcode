import random
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.dict = {}
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = "0123456789"
        url = "".join(random.sample(lower+upper+number,6))
        url = "http://tinyurl.com/" + url
        self.dict[longUrl] = url
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        for i in self.dict.keys():
            return i
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

