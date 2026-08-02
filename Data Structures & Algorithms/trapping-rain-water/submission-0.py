class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        count = 0
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        for i in range(0,len(height)):
            max_left[i] = left
            if height[i] > left:
                left = height[i]
        j = len(height)-1
        while j >-1:
            max_left[j] = min(right,max_left[j])
            if height[j] > right:
                right = height[j]
            j-=1
        for i in range(0,len(height)):
            if max_left[i]- height[i] >0:
                count +=max_left[i] - height[i]
    
        print(max_left)
        return count   