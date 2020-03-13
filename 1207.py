class Solution:
    def uniqueOccurrences(self, arr) :
            s = set(arr)
            cnt = []
            for i in s:
                cnt.append(arr.count(i))
            if len(list(set(cnt))) ==len(cnt):
                return True
            else:
                return False
s = Solution()
a = [-3,0,1,-3,1,1,1,-3,10,0,0]
print(s.uniqueOccurrences(a))
