# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        if n == 0:
            return []
        steps = []
        steps.append(pairs.copy())
        for i in range(n-1):
            j = i + 1
            el = pairs[j]
            j -= 1
            while el.key < pairs[j].key and j >= 0:
                pairs[j+1] = pairs[j]
                j -= 1  
                pairs[j+1] = el
            steps.append(pairs.copy())

        return steps

