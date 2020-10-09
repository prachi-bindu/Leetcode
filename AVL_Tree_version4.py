class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.ht = 1
        
class AVL_Tree:
    def insert(self, val, rootNode):
        #if the tree does not contain any node
        if not rootNode:
            return Node(val)
            
        elif val < rootNode.val:
            rootNode.left = insert(val,rootNode.left)
            return rootNode.left
            
        elif val > rootNode.val:
            rootNode.right = insert(val, rootNode.right)
            return rootNode.right

    def delete(self, val, rootNode):
        if not rootNode:
            return
            