class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        freq_t = {}
        for letter in t:
            freq_t[letter] = freq_t.get(letter, 0) + 1
        
        start_index = -1
        min_length = len(s) + 1
        l = 0
        r = 0
        match = 0
        freq_window = {}
        while  r < len(s):
            if s[r] not in freq_t:
                r += 1
                continue
            
            freq_window[s[r]] = freq_window.get(s[r], 0) + 1
            if freq_window[s[r]] == freq_t[s[r]]:
                match += 1
            
            while match == len(freq_t):
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    start_index = l
                if s[l] in freq_window:
                    freq_window[s[l]] -= 1
                    if freq_window[s[l]] < freq_t[s[l]]:
                        match -= 1
                l += 1
            
            r += 1
        
        if min_length > len(s):
            return ''
        return s[start_index: start_index + min_length]
