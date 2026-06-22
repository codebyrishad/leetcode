class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp=s.split()[-1]
        return len(temp)