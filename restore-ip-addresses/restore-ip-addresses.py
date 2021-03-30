class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not 4 <= len(s)<=12:
            return []
        
        def helper(idx,curr):
            nonlocal result
            #terminal condition
            if len(curr) ==4:
                if idx == len(s):
                    result.append('.'.join(curr))
                return
            #recursive condition
            num = ''
            for i in range(idx,min(idx+3,len(s))):
                num += s[i]
                #no leading zero 
                if num[0] == "0" and len(num)>1:
                    break
                
                # between zero and 255
                if 0 <= int(num)<=255:
                    curr.append(num)
                    helper(i+1,curr)
                    curr.pop()
                      
        result = []
        helper(0,[])
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def valid(segment):
#             return int(segment)<=255 if segment[0]!='0' else len(segment)==1
        
#         def update_output(curr_pos):
#             segment = s[curr_pos+1:n]
#             if valid(segment):
#                 segments.append(segment)
#                 output.append('.'.join(segments))
#                 segments.pop()
        
#         def backtrack(prev_pos=-1,dots =3):
#             for curr_pos in range(prev_pos+1,min(n-1,prev_pos+4)):
#                 segment = s[prev_pos+1:curr_pos+1]
#                 if valid(segment):
#                     segments.append(segment)
                    
#                     if dots-1==0:
#                         update_output(curr_pos)
#                     else:
#                         backtrack(curr_pos,dots-1)
                    
#                     segments.pop()
#         n = len(s)
#         output,segments = [],[]
#         backtrack()
#         return output
            
                