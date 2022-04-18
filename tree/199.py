# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
#  示例 1:
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#
from typing import Optional, List

import utils.tree
from utils.tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        levelQ,nextQ= [root],[]
        while len(levelQ) is not 0:
            cur = levelQ.pop(0)
            if cur.left is not None:
                nextQ.append(cur.left)
            if cur.right is not None:
                nextQ.append(cur.right)

            if len(levelQ) is 0:
                # if len of levelQ is 0 means cur is the rightest node
                res.append(cur.val)
                levelQ,nextQ = nextQ,[]

        return res





if __name__ == '__main__':
    root = utils.tree.new_tree_from_level_str("[1,2,3,4]")
    s = Solution()
    x = s.rightSideView(root)
    print(x)