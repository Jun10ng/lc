from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1),len(grid1[0])
        father = [-1]*(m*n)
        cnt,visited = 0,[False]*m*n
        def getGridIdx(i,j)->int:
            return j*n+i

        def find(x)->int:
            if father[x]!=-1:
                return find(father[x])
            return x

        def merge(f,c):
            ff = find(f)
            father[c] = ff

        def buildGrid1DFS(i,j,f):
            if i >= m or j >=n:
                return
            if grid1[i][j] == 0:
                return
            idx = getGridIdx(i,j)
            if visited[idx]:
                return

            if f==-1:
                # ist unit of grid
                f = idx
            else:
                merge(f,idx)

            for v in [[-1,0],[0,-1],[1,0],[0,1]]:
                visited[idx] = True
                newi,newj = i+v[0],j+v[1]
                buildGrid1DFS(newi,newj,f)
                visited[idx] = False

        def compareGrid2DFS(i,j,f):
            if i >= m or j >=n:
                return
            if grid2[i][j] == 0:
                return
            idx = getGridIdx(i,j)

            for v in [[-1,0],[0,-1],[1,0],[0,1]]:
                visited[idx] = True
                newi,newj = i+v[0],j+v[1]
                compareGrid2DFS(newi,newj,f)
                visited[idx] = False