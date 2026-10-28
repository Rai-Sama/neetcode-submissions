def two_sum(a, t, n, f):
    i, j = f+1, n-1
    ires = []
    while i < j:
        val = a[i] + a[j]
        if val > t:
            j -= 1
        
        elif val < t:
            i += 1
        
        else:
            ires.append([a[i], a[j]])
            i += 1
            j -= 1

    return ires



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
                for p in pair:
                    tmp = [t]
                    tmp.extend(p)
                    res.append(tmp)
            i += 1
        
        #print(res)
        return list(map(list, dict.fromkeys(map(tuple, res))))
            