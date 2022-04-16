
from typing import List, Optional
from utils.tree import *
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postTrace(root,result)
        return result

    def postTrace(self,root: Optional[TreeNode],result):
        if root is None:
            return

        self.postTrace(root.left,result)
        self.postTrace(root.right,result)
        result.append(root.val)
        return

if __name__ =='__main__':
    s = Solution()
    level = '[1,null,2,3]'
    r = new_tree_from_level_str(level)
    # print(level_trace(r))
    print(s.postorderTraversal(r))