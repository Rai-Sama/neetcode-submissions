class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {}

        for i in nums:
            if i in cnts:
                cnts[i] += 1
            else:
                cnts[i] = 1
        lst = []
        for i, cnt in cnts.items():
            lst.append((cnt, i))

        lst.sort(reverse=True)

        return [i[1] for i in lst[:k]]
