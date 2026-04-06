class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        freq = {}
        maxLength = 0
        while l <= r and r < len(s):
            print(freq, r, s[r])
            while freq.get(s[r], 0) > 0:
                freq[s[l]] -= 1
                l += 1
            freq[s[r]] = 1
            r += 1
            length = r - l
            maxLength = max(maxLength, length)
        return maxLength