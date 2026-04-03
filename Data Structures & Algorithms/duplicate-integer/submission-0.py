class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existingNumbers = set()
        for num in nums:
            if num in existingNumbers:
                return True
            
            existingNumbers.add(num)
        
        return False
        