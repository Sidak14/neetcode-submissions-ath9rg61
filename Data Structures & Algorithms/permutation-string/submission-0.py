class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        for letter in s1:
            s1Freq[letter] = s1Freq.get(letter, 0) + 1
        
        l = 0
        r = 0
        slidingFreq = {}
        while r < len(s2):
            print(slidingFreq, l, s2[l], r, s2[r])
            if s2[r] not in s1Freq:
                slidingFreq = {}
                l = r + 1
                r = r + 1
                continue
            
            slidingFreq[s2[r]] = slidingFreq.get(s2[r], 0) + 1
            while slidingFreq[s2[r]] > s1Freq[s2[r]]:
                slidingFreq[s2[l]] -= 1
                l += 1
            
            #slidingFreq[s2[r]] <= s1Freq[s2[r]]
            if r - l + 1 == len(s1):
                return True
            r += 1
        
        return False