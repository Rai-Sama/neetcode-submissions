class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        tot = 0

        for i, right in enumerate(height):
            while stack and right > height[stack[-1]]:

                flr = stack.pop() # Floor
                
                if not stack: # No left wall
                    break
                
                left = stack[-1]
                l = i - left - 1
                h = min(right, height[left]) - height[flr]
                tot += l*h

            stack.append(i)
        
        return tot


