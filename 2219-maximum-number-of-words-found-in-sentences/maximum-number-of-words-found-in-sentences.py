class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        temp=""
        max_word=""
        for i in sentences:
            temp=i.split()
            if len(temp) > len(max_word):
                max_word=temp
        return len(max_word)  
                