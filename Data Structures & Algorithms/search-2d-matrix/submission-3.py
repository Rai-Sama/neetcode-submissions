def binSrch(lst, target, l, r):
    if l > r:
        return False
    if l == r:
        return lst[l] == target
    
    mid = (l+r)//2

    if lst[mid] == target:
        return True
    
    if lst[mid] < target:
        return binSrch(lst, target, mid+1, r)
    else:
        return binSrch(lst, target, l, mid-1)
    


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Blow matrix up to a 1D array of length m*n
        # 2. Binary search

        lst = [j for i in matrix for j in i]
        return binSrch(lst, target, 0, len(lst)-1)