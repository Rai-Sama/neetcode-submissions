class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {}
        lst = [[] for i in range(len(nums) + 1)]
        res = []
        for i in nums:
            cnts[i] = 1 + cnts.get(i, 0)

        for i, j in cnts.items():
            lst[j].append(i)
            
        for i in lst[::-1]:
            if i:
                for j in i:
                    res.append(j)
                    k -= 1
                    if k <= 0:
                        return res
        
        return res