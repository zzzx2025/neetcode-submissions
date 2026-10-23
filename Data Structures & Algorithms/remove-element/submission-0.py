class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        some_val = 0
        for i in range(len(nums)):
            if nums[i] == val:
                some_val += 1
        nums.sort()
        for j in range(len(nums) - 1):
            if nums[j] == val:
                for k in range(j + 1, len(nums)):
                    temp = nums[k]
                    nums[k] = nums[j]
                    nums[j] = temp
        k = len(nums) - some_val
        return k