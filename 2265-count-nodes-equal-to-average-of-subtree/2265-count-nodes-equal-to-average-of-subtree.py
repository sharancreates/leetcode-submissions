# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes_count = 0
        
        def calculate_subtree_stats(node):
            if not node:
                return 0, 0 
            
            left_sum, left_count = calculate_subtree_stats(node.left)
            right_sum, right_count = calculate_subtree_stats(node.right)
            
            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count
            
            if node.val == current_sum // current_count:
                self.matching_nodes_count += 1
                
            return current_sum, current_count

        calculate_subtree_stats(root)
        return self.matching_nodes_count
