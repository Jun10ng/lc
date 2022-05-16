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
        # disjoint union count, parent list
        cnt,father = n,[-1]*n

        def find(x)->int:
            if father[x]!=-1:
                return find(father[x])
            return x

        def merge(f,c)->bool:
            if c == -1:return True
            if father[c] != -1:
                # in Binary Tree, a child node only has a parent
                return False
            ff = find(f)
            fc = find(c)
            if fc == f:
                return False
            if ff == fc and ff != -1:
                # there is a cycle
                return False

            father[c] = f
            nonlocal cnt
            cnt = cnt - 1
            return True

        # build union-query set
        for i in range(n):
            leftChildVal,rightChildVal = leftChild[i],rightChild[i]
            if not (merge(i,leftChildVal) and merge(i,rightChildVal)):
                return False

        return cnt == 1




if __name__ == '__main__':
    s = Solution()
    # True
    print(s.validateBinaryTreeNodes(4,[3,-1,1,-1],[-1,-1,0,-1]))

    # False
    print(s.validateBinaryTreeNodes(4,[1,-1,3,-1],[2,3,-1,-1]))
    # False
    print(s.validateBinaryTreeNodes(4,[1,0,3,-1],[-1,-1,-1,-1]))


