class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char
        
        return newStr == newStr[::-1]