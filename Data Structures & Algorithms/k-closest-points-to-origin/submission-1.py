import math

class Solution:
    def quicksort(self, points: List[List[int]], arr: list[float], s: int, e: int) -> list[float]:
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        pivot1 = points[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                temp1 = arr[left]
                temp2 = points[left][:]
                arr[left] = arr[i]
                points[left][:] = points[i][:]
                arr[i] = temp1
                points[i][:] = temp2
                left += 1

        arr[e] = arr[left]
        points[e] = points[left]
        arr[left] = pivot
        points[left] = pivot1

        self.quicksort(points, arr, s, left - 1)
        self.quicksort(points, arr, left + 1, e)

        return arr
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 1 and len(points) == 1:
            return points
        
        dis = []

        for i in range(len(points)):
            r = points[i]
            temp = math.sqrt((r[0] - 0)**2 + (r[1] - 0)**2)
            dis.append(temp)

        self.quicksort(points, dis, 0, len(dis) - 1)

        return points[:k]
        
    