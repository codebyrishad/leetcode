class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        len(nums) != len(set(nums))
        
        if len(nums) == len(set(nums)):
            return False
        else:
            return True