class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq_s = {}
        for letter in s:
            freq_s[letter] = freq_s.get(letter, 0) + 1
        
        output = []
        i = 0
        while i < len(s):
            start = i
            freq_substr = {}
            freq_substr[s[i]] = 1
            queue = deque(s[i])
            while queue:
                letter = queue.popleft()
                while freq_substr[letter] != freq_s[letter]:
                    i += 1
                    if s[i] not in freq_substr:
                        freq_substr[s[i]] = 0
                        queue.append(s[i])
                    freq_substr[s[i]] += 1
            output.append(i - start + 1)
            i += 1

        return output