class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        flgAdded = False
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                output.append(intervals[i])
                i += 1
                continue
            
            if intervals[i][0] > newInterval[1]:
                if not flgAdded:
                    output.append(newInterval)
                    flgAdded = True
                output.append(intervals[i])
                i += 1
                continue
            
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        
        if not flgAdded:
            output.append(newInterval)
        
        print(newInterval)
        return output