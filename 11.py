"""给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
 """


class Solution:  # 超时
    def maxArea(self, height) -> int:
        """

        :param height: list[int]
        :return: int
        """
        m = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                if min(height[i], height[j]) * (j - i) > m:
                    m = min(height[i], height[j]) * (j - i)
        return m


class Solution2:
    def maxArea(self, height) -> int:
        """
        :param height: list[int]
        :return: int
        """
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


s = Solution2()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
