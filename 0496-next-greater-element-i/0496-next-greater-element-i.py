class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            index=nums2.index(i)
            for j in range(index+1,len(nums2)):
                if nums2[j]>i:
                    arr.append(nums2[j])
                    break
            else:
                arr.append(-1)
        return arr

        