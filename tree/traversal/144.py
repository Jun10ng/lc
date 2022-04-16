# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
from typing import List, Optional
from utils.tree import *

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        result = []
        self.preTrace(root,result)
        return result

    def preTrace(self,root: Optional[TreeNode],result):
        if root is None:
            return
        result.append(root.val)
        self.preTrace(root.left,result)
        self.preTrace(root.right,result)

if __name__ =='__main__':
    s = Solution()
    level = '[1,null,2,3]'
    r = new_tree_from_level_str(level)
    # print(level_trace(r))
    print(s.preorderTraversal(r))



