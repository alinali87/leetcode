class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(node) -> int:
            if node.left is None and node.right is None:
                return 1
            if node.left and node.right:
                return max(height(node.left), height(node.right)) + 1
            elif node.left:
                return height(node.left) + 1
            else:
                return height(node.right) + 1


        def find_depth(root) -> int:
            if root is None:
                return 0
            depth = height(root)
            return depth
        
        return find_depth(root)
