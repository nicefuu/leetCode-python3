"""二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。
给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。"""
class Solution:
    def readBinaryWatch(self, num):
        """
        :param num:int
        :return:list[str]
        """

class Solution2:
    def readBinaryWatch(self, num):
        """
        :param num: int
        :return:list[str]
        """
        hour_arr = [[], [], [], []]
        for i in range(12):
            hour_arr[str(bin(i)).count('1')].append(str(i))
        minute_arr = [[], [], [], [], [], []]
        for i in range(60):
            if 0 <= i <= 9:
                minute_arr[str(bin(i)).count('1')].append('0' + str(i))
            else:
                minute_arr[str(bin(i)).count('1')].append(str(i))
        r_arr = []
        for h in range(num+1):
            m = num -h
            if 0 <= h <= 3 and 0 <= m <= 5:
                for i in range(len(hour_arr[h])):
                    for j in range(len(minute_arr[m])):
                        r_arr.append(hour_arr[h][i]+":"+minute_arr[m][j])
        return r_arr
s=Solution2()
n=2
print(s.readBinaryWatch(n))
