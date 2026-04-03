class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lettersInS = {}
        for letter in s:
            if letter not in lettersInS:
                lettersInS[letter] = 0
            lettersInS[letter] += 1
        
        for letter in t:
            if letter not in lettersInS:
                return False
            lettersInS[letter] -= 1
            if lettersInS[letter] < 0:
                return False
        
        return True