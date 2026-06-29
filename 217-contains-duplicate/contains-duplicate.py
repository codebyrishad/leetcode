class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) != len(set(nums))
        
        if len(nums) == len(set(nums)):
            return False
        else:
            return True