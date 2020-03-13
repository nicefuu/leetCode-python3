class Solution:
    def sortByBits(self, arr):
        for i in range(len(arr)):
            arr[i] = arr[i] + 1000 * str(bin(arr[i])).count('1')
        arr.sort()
        for i in range(len(arr)):
            if arr[i]!=0:
               arr[i] =int(str(arr[i])[len(str(arr[i]))-3:])
        return arr
s= Solution()
print(s.sortByBits( [2,3,5,7,11,13,17,19]))

