class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        grades_by_id = collections.defaultdict(list)
        res = []
        for student_id,grade in items:
            if student_id in grades_by_id:
                grades_by_id[student_id] += [grade]
            else:
                grades_by_id[student_id].append(grade)
                
        for key,value in grades_by_id.items():
            value.sort()
            res.append( (key,self.calculate(value[-5::]) ))
        
        res.sort()
        return res
                          
    def calculate(self,values):
        return (sum(values)//5) 
        