class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr=[-1]*len(nums)
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                next_index=(i+j)%len(nums)
                if nums[next_index]>nums[i]:
                    arr[i]=nums[next_index]
                    break
        return arr

        