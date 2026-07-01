class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq=sorted(set(nums))
        k=len(unq)
        nums[:k]=unq
        return k
        
        