class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r)//2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                r = mid-1
            else:
                l = mid
        return -1
