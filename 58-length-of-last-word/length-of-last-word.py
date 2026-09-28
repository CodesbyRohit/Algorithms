class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces at the end of the string
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length