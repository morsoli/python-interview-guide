#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if height==[]:
            return 0
        area=0
        # 定义两个指针
        p1=0
        p2=len(height)-1
        while p1<p2:
            # 容器的容量
            area=max(area,min(height[p1],height[p2])*(p2-p1))
            # 短板作为移动的判断条件
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return area
