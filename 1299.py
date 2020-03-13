"""
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
完成所有替换操作后，请你返回这个数组。
示例：
输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]"""


class Solution:
    def replaceElements(self, arr):
        """
        :param arr: list[int]
        :return: list[int]
        """
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            elif i == len(arr) - 2:
                arr[i] = arr[i + 1]
            else:
                t = arr[i + 1]
                j = i + 1
                while j < len(arr) - 1:
                    if t < arr[j + 1]:
                        t = arr[j + 1]
                    j += 1
                arr[i] = t
        return arr


class Solution2:
    def replaceElements(self, arr):
        """
        :param arr: list[int]
        :return: list[int]
        """
        m = -1
        for i in range(1, len(arr)):
            if arr[-i] > m:
                m = arr[-i]
            arr[-i] = m
        arr = arr[1:]
        arr.append(-1)
        return arr


s = Solution2()
a = [17, 18, 5, 4, 6, 1]
b = [23, 12, 2, 7, 4, 5, 6]
# -1 6 6 6 7 7 12
print(s.replaceElements(b))
