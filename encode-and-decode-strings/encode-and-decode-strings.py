class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return(chr(258))
        
        return chr(257).join(x for x in strs)
        # enc =""
        # for i in range(len(strs)):
        #     if i == 0:
        #         enc += strs[i]
        #     else:
        #         enc += "#" + strs[i]
        # # print(enc)
        # return enc

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        
        return s.split(chr(257))
        # dec = s.split("#")
        # return dec
        # pass

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))