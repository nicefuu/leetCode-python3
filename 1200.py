"""
给你个整数数组 arr，其中每个元素都 不相同。
请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
示例 1：
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
示例 2：

输入：arr = [1,3,6,10,15]
输出：[[1,3]]
示例 3：

输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]"""


class Solution:
    def minimumAbsDifference(self, arr):
        """
        :param arr:list[int]
        :return: list[list[int]]
        """
        arr.sort()
        r=[]
        m = arr[-1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] <= m:
                m = arr[i + 1] - arr[i]
        for i in range(len(arr)-1):
           if arr[i+1]-arr[i]==m:
               r.append([arr[i],arr[i+1]])
        return r
s=Solution()
print(s.minimumAbsDifference([4,2,1,3]))
print(s.minimumAbsDifference([1,3,6,10,15]))
print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))