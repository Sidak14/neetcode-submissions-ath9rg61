class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices = {}
        for i in range(len(s)):
            last_indices[s[i]] = i

        output = []
        i = 0
        while i < len(s):
            startIndex = i
            lastIndex = last_indices[s[i]]
            while i < lastIndex:
                i += 1
                lastIndex = max(lastIndex, last_indices[s[i]])
            
            i += 1
            output.append(i - startIndex)
        
        return output