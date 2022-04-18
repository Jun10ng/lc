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
from collections import defaultdict
from typing import Optional, List

import utils.tree
from utils.tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res,dict = [],defaultdict(list)
        if not root:
            return res

        def preTrace(curNode,index):
            if not curNode:
                return
            dict[index].append(curNode.val)
            preTrace(curNode.left,index+1)
            preTrace(curNode.right,index+1)

        preTrace(root,0)

        res = [v[-1] for v in dict.values()]

        return res





if __name__ == '__main__':
    root = utils.tree.new_tree_from_level_str("[1,2,3,4]")
    s = Solution()
    x = s.rightSideView(root)
    print(x)