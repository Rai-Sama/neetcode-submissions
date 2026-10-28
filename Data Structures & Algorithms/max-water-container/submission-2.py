class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        mx = 0
        while i < j:
            l = j - i
            if heights[i] < heights[j]:
                h = heights[i]
                i += 1
                while i < j and heights[i] < h:
                    i += 1
            elif heights[j] < heights[i]:
                h = heights[j]
                j -= 1
                while i < j and heights[j] < h:
                    j -= 1
            else:
                h = heights[i]
                i += 1
                j -= 1


            mx = max(mx, h*l)
        return mx
