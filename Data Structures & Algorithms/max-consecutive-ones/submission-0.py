class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxnum = 0
        currentnum = 0
        for i in range(len(nums)):
            if nums[i] == 1 and i == 0:
                maxnum += 1
            elif nums[i] == 1:
                maxnum += 1
            else:
                maxnum = 0
            if maxnum > currentnum:
                currentnum = maxnum
        return currentnum