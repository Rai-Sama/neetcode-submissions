def binSrch(lst, l, r, target):
    if l >= r:
        return l, lst[l] == target
    
    mid = (l + r)//2
    if lst[mid] == target:
        return mid, True
    
    if lst[mid] < target:
        return binSrch(lst, mid+1, r, target)
    else:
        return binSrch(lst, l, mid-1, target)
    


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Binary search on 1st column
        # 2. Binary search on last searched row

        col = [i[0] for i in matrix]
        indx, found = binSrch(col, 0, len(col)-1, target)
        if found:
            return True
        
        _, found = binSrch(matrix[indx], 0, len(matrix[indx])-1, target)
        return found