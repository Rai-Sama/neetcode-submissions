class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        vals = []
        for idx, i in enumerate(points):
            vals.append([i[0]**2 + i[1]**2, idx])
        vals.sort()
        res = []
        for i in range(k):
            res.append(points[vals[i][1]])
        
        
        return res