class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            bracket_type = letter
            
            closing = True
            if letter == '}':
                bracket_type = '{'
            elif letter == ')':
                bracket_type = '('
            elif letter == ']':
                bracket_type = '['
            else:
                closing = False
            
            if closing == False:
                stack.append(bracket_type)
                continue
            
            if len(stack) == 0:
                return False

            if stack.pop() != bracket_type:
                return False
        
        if len(stack) > 0:
            return False
        
        return True
            
