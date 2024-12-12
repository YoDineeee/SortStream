class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[L - 2]:
                nums[L] = nums[i]
                L += 1 

        return L