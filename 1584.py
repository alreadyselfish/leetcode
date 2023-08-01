class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        par = [i for i in range(len(points))]
        child = [1 for i in range(len(points))]
        def dis(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            return abs(x2 - x1) + abs(y2 - y1) #constant time 
        def find(p):
            while par[p] != p:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2:
                return False
            if child[p1] > child[p2]:
                child[p1] += child[p2]
                par[p2] = p1
            else:
                child[p2] += child[p1]
                par[p1] = p2
            return True
        heap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                heapq.heappush(heap, (dis(i, j), i, j)) #O(n^2) time | n = len(points)
        cost = 0
        while len(heap)>0:
            w, c1, c2 = heapq.heappop(heap)
            flag = union(c1, c2)
            if flag:
                cost += w
        return cost


        

        