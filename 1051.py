"""学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。
示例：
输入：heights = [1,1,4,2,1,3]
输出：3

"""
class Solution:
    def heightChecker(self, heights):
        """
        :param heights:list[int]
        :return: int
        """
        cnt=0
        h = sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=h[i]:
                cnt+=1
        return cnt
s=Solution()
a=[1,1,4,2,1,3]
print(s.heightChecker(a))
