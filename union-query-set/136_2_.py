# 第二次尝试AC 136题

# 二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。
#
#  只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。
#
#  如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。
#
#  输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# 输出：true
#
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        father,cnt = [-1]*n,n

        # cNode 的父亲是fNode
        def union(fNode,cNode) -> bool:
            if father[cNode] != -1:
                return False
            father[cNode] = fNode

            nonlocal cnt
            cnt=cnt-1
            return True

        for i in range(n):
            for child in [leftChild[i],rightChild[i]]:
                if child!=-1:
                    if not union(i,child):
                        return False

        return cnt == 1

if __name__ == '__main__':
    s = Solution()
    print(s.validateBinaryTreeNodes(4,[1,-1,3,-1],[2,-1,-1,-1]))



