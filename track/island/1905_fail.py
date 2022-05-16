from typing import List

# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖
# 直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。
#
#  如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，那
# 么我们称 grid2 中的这个岛屿为 子岛屿 。
#
#  请你返回 grid2 中 子岛屿 的 数目 。
#
#
#
#  示例 1：
#
#  输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# 输出：3

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ret = 0
        n,m  = len(grid2),len(grid2[0])
        q = list()

        def bfs(i,j) -> bool:
            check = (grid1[i][j] == 1)
            q.append([i,j])
            while len(q) != 0:
                e = q.pop()
                si,sj = e[0],e[1]
                grid2[si][sj] = 0
                for [ni,nj]in [[si-1,sj],[si+1,sj],[si,sj-1],[si,sj+1]]:
                    if ni<0 or nj <0 or ni >= n or nj >= m or grid2[ni][nj]==0:
                        continue
                    q.append([ni,nj])
                    check = check and (grid1[ni][nj]==1)
            return check

        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    ret = ret + int(bfs(i,j))

        return ret


if __name__ == '__main__':
    g1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    g2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    s= Solution()
    ret = s.countSubIslands(g1,g2)
    print(ret)




