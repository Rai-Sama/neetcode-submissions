class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        mx = 0
        for i in snums:
            if i - 1 not in snums:
                tmp = 1
                while i + tmp in snums:
                    tmp += 1
            mx = max(mx, tmp)

        return mx    
