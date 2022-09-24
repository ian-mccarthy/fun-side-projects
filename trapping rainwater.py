
#Given an array of non-negative integers "height_list[]" representing an elevation map where the width of each bar is 1,
#compute how much water it is able to trap after raining.

class Solution:
    def __init__(self) -> None:
        pass

    def trap(self, height: list[int]) -> int:
        
        if not height: 
            return 0
        
        l, r = 0, len (height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0
        
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max (leftMax, height [l])
                result += leftMax - height [l]
                
            else:
                r -= 1
                rightMax = max (rightMax, height [r])
                result += rightMax - height [r]
                
        return result

height_list = [0,1,0,2,1,0,1,3,2,1,2,1] 

#other examples to try: 
# [4,2,0,3,2,5] [2, 0, 2] [3, 0, 2, 0, 4]

trw_instance = Solution ()
rainwater_Trapped = trw_instance.trap(height_list)

print (rainwater_Trapped)
