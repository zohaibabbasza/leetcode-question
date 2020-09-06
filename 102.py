# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

class Solution:
    def levelOrder(self, root):
        pass



if __name__ == "__main__":
    r = TreeNode(50) 
    insert(r,TreeNode(30)) 
    insert(r,TreeNode(20)) 
    insert(r,TreeNode(40)) 
    insert(r,TreeNode(70)) 
    insert(r,TreeNode(60)) 
    insert(r,TreeNode(80)) 
    inorder(r) 