class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:return 0
        if len(heights)==1:return heights[0]
        maxarea=0
        stack=[0]
        for i in range(1,len(heights)):
            if heights[i]<heights[i-1]:
                while stack and heights[stack[-1]]>heights[i]:
                    idx=stack.pop()
                    area=heights[idx]*(i-stack[-1]-1) if stack else heights[idx]*i
                    maxarea=max(maxarea,area)
            stack.append(i)
        while stack:
            idx=stack.pop()
            area=heights[idx]*(len(heights)-stack[-1]-1) if stack else heights[idx]*len(heights)
            maxarea=max(maxarea,area)
        return maxarea
