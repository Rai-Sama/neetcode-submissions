def two_sum(a, t, n, f):
    i, j = f+1, n-1

    while i < j:
        val = a[i] + a[j]
        if val > t:
            j -= 1
        
        elif val < t:
            i += 1
        
        else:
            return [a[i], a[j]]

    return []



class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        i = 0
        res = []

        while i < n-1:
            t = nums[i]
            pair = two_sum(nums, -t, n, i)

            if pair:
                tmp = [t]
                tmp.extend(pair)
                res.append(tmp)
            i += 1
        
        #print(res)
        return list(map(list, dict.fromkeys(map(tuple, res))))
            