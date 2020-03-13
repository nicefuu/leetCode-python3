class Solution:
    def minTimeToVisitAllPoints(self, points):
        count = 0
        if len(points)==0:
            return 0
        for i in range(len(points)-1):
            count += max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
        return count
