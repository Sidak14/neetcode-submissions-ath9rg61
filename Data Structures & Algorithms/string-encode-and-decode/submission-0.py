class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            output += str(len(s)) + '#'
            output += s
        
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            
            j = i + 1
            num = int(num)
            outputString = ''
            while j < (i + 1) + num:
                outputString += s[j]
                j += 1
            output.append(outputString)
            i = j

        return output