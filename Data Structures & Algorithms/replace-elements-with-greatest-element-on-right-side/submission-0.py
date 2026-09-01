class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        mx = arr[-1]
        arr[-1] = -1
        while i >= 0:
            arr[i], mx = mx, max(arr[i], mx)
            i -= 1

        return arr