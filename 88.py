"""给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。


说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。


示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]"""


class Solution:
    def merge(self, nums1, m, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        print(nums1)
        return None


class Solution2:
    def merge(self, nums1, m, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_index = 0
        if m == 0:
            for i in range(n):
                nums1[i]=nums2[i]
        else:
            index1 = 0
            for index2 in range(n):
                while index1 < m+index2:
                    if nums2[index2] > nums1[index1]:
                        index1 += 1
                    else:
                        break
                t = m + index2
                while t > index1:
                    nums1[t] = nums1[t - 1]
                    t -= 1
                nums1[index1] = nums2[index2]
        print(nums1)
        return



s = Solution2()
s.merge(nums1=[0], m=0, nums2=[1], n=1)
