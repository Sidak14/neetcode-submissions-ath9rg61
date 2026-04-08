class Solution:
    def checkValidString(self, s: str) -> bool:
        opening_brackets = []
        astericks = []
        for i in range(len(s)):
            letter = s[i]
            if letter == '(':
                opening_brackets.append(i)
                continue
            
            if letter == '*':
                astericks.append(i)
                continue
            
            # letter == ')'
            if len(opening_brackets) > 0:
                opening_brackets.pop()
                continue
            
            if len(astericks) > 0:
                # count an astrick as an opening bracket
                astericks.pop()
                continue
            
            return False
        
        while opening_brackets:
            if not astericks:
                return False
            
            bracket_index = opening_brackets.pop()
            asterick_index = astericks.pop()
            if bracket_index > asterick_index:
                return False
        
        return True
            

        