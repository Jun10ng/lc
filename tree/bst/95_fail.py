# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
import copy
from typing import List

import utils.tree
from utils.tree import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []
        # 生成 start 到 end之间的所有树排列
        def trace(start, end)->[]:
            if end < start:
                return [None,]

            allTrees = []
            for i in range(start,end+1):
                leftAll = trace(start,i-1)
                rightAll = trace(i+1,end)
                for left in leftAll:
                    for right in rightAll:
                        curN = TreeNode(i)
                        curN.left = left
                        curN.right = right
                        allTrees.append(curN)
            return allTrees

        return trace(1, n) if n else []

if __name__ == '__main__':
    s = Solution()
    res = s.generateTrees(3)
    for t in res:
        print(utils.tree.level_trace(t))
