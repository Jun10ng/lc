from typing import Optional, List

from utils.tree import TreeNode

from utils.tree import new_tree_from_level_str


# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.trace(root, result)
        return result

    def trace(self, root: Optional[TreeNode], result):
        if root is None:
            result = []
        if root is None:
            return None

        if root.left is not None:
            self.trace(root.left, result)

        result.append(root.val)

        if root.right is not None:
            self.trace(root.right, result)


if __name__ == '__main__':
    s = Solution()
    level = '[1,null,2,3]'
    r = new_tree_from_level_str(level)

    print(s.inorderTraversal(r))
