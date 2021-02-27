
def lengthOfLongestSubstring(s: str) -> int:
    i,j = 0,0
    result = []
    count = 0
    
    while(j<len(s)):
        if s[i] != s[j] and i!=j:
            j = j+1
            count = count+1
        elif s[i] == s[j] and i==j:
            j = j+1
            count = count+1
        elif s[i] == s[j] and i!=j:
            i = j
            result.append(count)
            count = 0
    
    return max(result)
    
if __name__ == '__main__': 
    lengthOfLongestSubstring("pwwkew")