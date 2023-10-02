# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right: 
                    return False
                return rec(node.left, left, node.val) and rec(node.right, node.val, right)
            return True
        return rec(root, -float('inf'), float('inf') )



# The code you provided is an implementation of a function isValidBST that checks whether a given binary tree is a valid binary search tree (BST) or not. A valid binary search tree is a binary tree where for each node:

# All nodes in its left subtree have values less than the node's value.
# All nodes in its right subtree have values greater than the node's value.

# Here's the approach and intuition used in this code:

# The function isValidBST takes a root node as its input, which represents the root of the binary tree.

# Inside the function, there is a recursive helper function rec that takes three arguments: node, left, and right. The node argument represents the current node being processed, and left and right represent the valid range of values that the current node's value must fall within.

# Within the rec function, there are several checks:

# If node is None, it means we've reached a leaf node or an empty subtree. In this case, we return True because an empty subtree is considered a valid BST.
# If the value of node is less than or equal to left or greater than or equal to right, it violates the BST property, so we return False.
# If none of the above conditions are met, we recursively call the rec function for the left and right subtrees of the current node:

# For the left subtree, we update the right argument to be the value of the current node 
# because all nodes in the left subtree must have values less than the current node's value.
# For the right subtree, we update the left argument to be the value of the current node because all nodes in the right subtree must have values greater than the current node's value.
# Finally, we call the rec function initially with the root node and initial range values of negative infinity (-float('inf')) for left and positive infinity (float('inf')) for right. This ensures that the entire tree is checked against the BST property.

# If the rec function returns True for the entire tree, 
# it means the tree is a valid BST, and the isValidBST function returns True. 
# Otherwise, it returns False.

# The key intuition here is to use a recursive approach to check each node in the binary tree 
# while maintaining the valid range of values that each node's value must fall within. 
# If any node violates the BST property, the function returns False, 
# and if all nodes satisfy the property, it returns True, indicating that the tree is a valid BST.


