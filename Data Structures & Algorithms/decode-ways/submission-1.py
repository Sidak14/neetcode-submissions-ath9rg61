class Solution:
    def numDecodings(self, s: str) -> int:
        numWays = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                continue
            
            # Count this letter by itself
            numWays[i] = numWays[i + 1] if i + 1 < len(s) else 1

            # if at end of the string
            if s[i] > '2' or i + 1 >= len(s):
                continue
            
            # Count '2x' or '1x'
            if (s[i] == '2' and s[i + 1] <= '6') or s[i] == '1':
                numWays[i] += numWays[i + 2] if i + 2 < len(s) else 1
        
        return numWays[0]

        