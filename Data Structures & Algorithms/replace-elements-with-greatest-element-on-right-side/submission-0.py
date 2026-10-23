class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for j in range(len(arr) -1, -1, -1):
            temp = arr[j]
            arr[j] = max_val
            max_val = max(max_val, temp)
        return arr