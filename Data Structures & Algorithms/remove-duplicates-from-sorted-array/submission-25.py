class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        num = len(nums)
        while num > 0:
            for i in range(len(nums) - 1):
                if nums[i] is nums[i+1]:
                    nums.pop(i)
                    break
            num -= 1
            """
        num = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                num.append(i)
        if len(num) == 1:
            nums.pop(num[0])
        else:
            num = num[::-1]
        
            for j in range(len(num)):
                nums.pop(num[j])
        return (len(nums))