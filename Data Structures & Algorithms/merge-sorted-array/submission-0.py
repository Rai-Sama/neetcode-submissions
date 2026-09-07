class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i < m:
            nums1[:] = nums3 + nums1[i:m]
        
        elif j < n:
            nums1[:] = nums3 + nums2[j:]

        else:
            nums1[:] = nums3

        