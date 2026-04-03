class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            
            freqs[num] += 1
        
        buckets = [[] for _ in range(len(nums))]
        for key in freqs:
            buckets[freqs[key] - 1].append(key)
        
        output = []
        for i in range(len(nums) - 1, -1, -1):
            if buckets[i] == []:
                continue
            
            if len(buckets[i]) >= k - len(output):
                for j in range(k - len(output)):
                    output.append(buckets[i][j])
                return output
            
            for num in buckets[i]:
                output.append(num)
        
        return output