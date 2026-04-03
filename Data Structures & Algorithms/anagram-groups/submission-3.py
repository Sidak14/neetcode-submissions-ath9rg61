class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsHash = {}
        base = ord('a')
        for s in strs:
            freq = [0 for _ in range(26)]
            for letter in s:
                freq[ord(letter) - ord('a')] += 1
            
            key = ''
            for f in freq:
                key += str(f) + '-'
            
            if key not in anagramsHash:
                anagramsHash[key] = []
            
            anagramsHash[key].append(s)
        
        output = []
        for key in anagramsHash:
            output.append(anagramsHash[key])

        return output