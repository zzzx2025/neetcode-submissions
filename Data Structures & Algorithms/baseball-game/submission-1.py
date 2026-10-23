class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for i in range(len(operations)):
            if operations[i] == '+':
                num = points[-1] + points[-2]
                points.append(num)
            elif operations[i] == 'D':
                num = 2 * points[-1]
                points.append(num)
            elif operations[i] =='C':
                points.pop()
            else:
                num = int(operations[i])
                points.append(num)            
        return sum(points)