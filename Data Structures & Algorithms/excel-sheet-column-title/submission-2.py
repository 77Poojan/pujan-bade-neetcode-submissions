class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        
        while columnNumber:
            columnNumber -= 1
            number =  (columnNumber % 26)
            s += chr(number + ord("A"))
            columnNumber = columnNumber // 26

        return s[::-1]