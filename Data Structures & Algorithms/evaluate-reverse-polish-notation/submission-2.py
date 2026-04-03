class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue
            
            top = stack.pop()
            second = stack.pop()
            result = 0
            if token == '+':
                result = top + second
            elif token == '-':
                result = second - top
            elif token == '*':
                result = second * top
            else:
                result = second / top
                result = int(result)
            
            stack.append(result)
        
        return stack.pop()