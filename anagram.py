def anagram(s1,s2):

    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    if len(s1)!=len(s2):
        return False
    
    temp = {}
    
    for letter in s1:
        if letter in temp:
            temp[letter] = temp[letter]+1
        else:
            temp[letter] = 1
    
    for letter in s2:
        temp[letter] = temp[letter]-1
    
    for k in temp:
        if temp[k]!=0:
            return False
    return True
