class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,target,issearch):
            left=0
            right=len(nums)-1
            ind=-1
            while left<=right:
                mid=(left+right)//2
                    
                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    ind=mid
                    if issearch:
                        right=mid-1
                    else:
                        left=mid+1
            return ind
        left=binary_search(nums,target,True)
        right=binary_search(nums,target,False)
        
        return [left,right]
