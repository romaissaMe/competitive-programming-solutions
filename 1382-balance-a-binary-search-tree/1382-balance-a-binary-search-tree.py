# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:     
        bst=[]
        def traverse(node):
            if node == None:
                return
            if node:
                if node.left: 
                    traverse(node.left)
                
                bst.append(node.val)

                if node.right: 
                    traverse(node.right)
        
        def balance(bst,start,end):
            if start>end:
                return None
            mid = start+(end-start)//2
            newNode = TreeNode(bst[mid]) 
            newNode.left = balance(bst,start,mid-1)
            newNode.right = balance(bst,mid+1,end)
            return newNode

        traverse(root)

        return  balance(bst,0,len(bst)-1)
                
    


            
