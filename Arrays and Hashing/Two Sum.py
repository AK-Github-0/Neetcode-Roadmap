class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target) and i != j:
                    return [i,j]
                j = j + 1
            i = i + 1
            
            
#brute force approach
#On^2 time complexity
