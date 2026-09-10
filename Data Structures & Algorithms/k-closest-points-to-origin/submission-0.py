class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        vals = []
        for idx, i in enumerate(points):
            vals.append([idx, abs(i[0]) +abs(i[1])])
        vals.sort()

        res = []
        for i in range(k):
            res.append(points[vals[i][0]])
        
        return res