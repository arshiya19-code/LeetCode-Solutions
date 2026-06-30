class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unq=sorted(set(nums),reverse=True)
        if len(unq)>=3:
            return unq[2]
        else:
            return unq[0]
        