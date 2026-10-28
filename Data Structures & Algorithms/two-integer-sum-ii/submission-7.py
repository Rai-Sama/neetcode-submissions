class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            t = numbers[i] + numbers[j]
            if t > target:
                j -= 1
            elif t < target:
                i += 1
            else:
                return [i + 1, j + 1]

