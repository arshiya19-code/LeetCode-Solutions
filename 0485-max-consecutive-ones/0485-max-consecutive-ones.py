class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        maxi=0
        for right in range(len(nums)):
            if nums[right]==0:
                left=right+1
            maxi=max(maxi,right-left+1)
        return maxi