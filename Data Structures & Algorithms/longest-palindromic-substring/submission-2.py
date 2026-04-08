class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        maxLength = 0
        startIndex = 0
        # for i in range(1.0, len(s) - 0.5, 0.5):
        for i in range(1, 2 * len(s) - 1):
            length = 0
            l = i // 2 - 1
            r = i // 2 + 1
            if i % 2 == 1:
                l = i // 2
                r = i // 2 + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l
            if length > maxLength:
                maxLength = length
                startIndex = l + 1
        
        return s[startIndex : startIndex + maxLength - 1]