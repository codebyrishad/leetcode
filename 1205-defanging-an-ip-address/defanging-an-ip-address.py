class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp=''
        for i in address:
            if i == ".":
                temp=temp+"[.]"
            else:
                temp=temp+i
        return temp        

        