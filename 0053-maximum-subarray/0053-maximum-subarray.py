class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=nums[0]
        sumi=0
        for i in range(n):
            sumi+=nums[i]
            maxi=max(maxi,sumi)
            if sumi<0:
                sumi=0
        return maxi
