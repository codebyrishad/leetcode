import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small_num=nums[0]
        large_num=nums[0]

        for i in nums:
            if i > large_num:
                large_num=i
            
            if i < small_num:
                small_num=i

        common_divisor = math.gcd(small_num, large_num)
        return common_divisor
        