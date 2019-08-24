#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        if m>n:
            nums1,nums2,m,n=nums2,nums1,n,m # 保持 n 始终大于 m
        if n==0:
            return None
        imin,imax,half_len=0,m,(n+m+1)/2
        while imin<=imax:
            # 确定 i j 两个值
            i=(imin+imax)/2
            j=half_len-i
            # i太小，应该增加
            if i<m and nums2[j-1]>nums1[i]:
                imin=i+1 
            # i太大，应该减小
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            # i 的值已经确定，现在找中间值
            else:
                # 确定左边界情况                
                if i==0:
                    max_of_left=nums2[j-1]
                elif j==0:
                    max_of_left=nums1[i-1]
                else:
                    max_of_left=max(nums1[i-1],nums2[j-1])
                # 奇数情况下
                if (m+n)%2==1:
                    return max_of_left
                # 确定右边界情况
                if i==m:
                    min_of_right=nums2[j]
                elif j==n:
                    min_of_right=nums1[i]
                else:
                    min_of_right=min(nums1[i],nums2[j])
                return (max_of_left+min_of_right)/2
