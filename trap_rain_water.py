'''

Trapping Rain Water:

We have heights of pillars that we essentially need to "trap" rain water inside of; that is, the rain should be
contained within the two pillars. We can get this by getting the minimum height between the two pillars (as that's as
much as can be "trapped") and then adding these values across the entire group of heights to get our sum.

The two pointers of both sides traverse each other, taking turns based on which side is less (and allows for both sides
to skip unimportant pillars). They get their height by getting the max of what was already found on their side, and
adding the max minus the height when the time comes.

This algorithm is less intuitive and does require a more holistic outlook, therefore there won't be code commentary
as this code is incredibly situational.

'''

class Solution:
    def trap(self, height):
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += (leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += (rightMax - height[r])
        return res