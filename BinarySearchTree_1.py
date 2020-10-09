class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
            
        else:
            self.__insertNode(value,self.root)
    
    def __insertNode(self,value,currentNode):
        #print("Hello from private method insertNode!")
        if value < currentNode.value:
            #print("vlaue<currentNode.value!")
            if currentNode.left == None:
                currentNode.left = Node(value)
                currentNode.left.parent = currentNode
            else:
                self.__insertNode(value,currentNode.left)
            
        elif value > currentNode.value:
            #print("vlaue>currentNode.value!")
            if currentNode.right == None:
                currentNode.right = Node(value)
                currentNode.right.parent = currentNode
            else:
                self.__insertNode(value,currentNode.right)
                
        else:
            print("Value already present in the tree!")
            
    def printTree(self):
        if self.root != None:
            self.__printTree(self.root)
            
    def __printTree(self, currentNode):
        if currentNode != None:
            self.__printTree(currentNode.left)
            print(currentNode.value)
            self.__printTree(currentNode.right)
            
    def height(self):
        if self.root == None:
            return 0
            
        else:
            return self.__height(self.root, 0)
            
    def __height(self, currentNode, ht):
        if currentNode == None: return ht
        leftSubtreeHt = self.__height(currentNode.left,ht+1)
        rightSubtreeHt = self.__height(currentNode.right,ht+1)
        height = max(leftSubtreeHt,rightSubtreeHt)
        return height
        
    def search(self,value):
        if self.root != None:
            return self.__search(self.root,value)
        else:
            return False
            
    def __search(self, currentNode, value):
        #check if the value is greater that or lesser than the root value and based upon the comparison, 
        #search in either left or right subtree recursively.
        if value == currentNode.value:
            return True
        
        elif value < currentNode.value and currentNode.left != None:
            return self.__search(currentNode.left,value)
            
        elif value > currentNode.value and currentNode.right != None:
            return self.__search(currentNode.right,value)
            
        else:
            return False

    def find(self, value):
        if self.root != None:
            return self.__find(self.root, value)
            
        else:
            print("Value not found!")
            
    def __find(self, currentNode, value):
        if currentNode.value == value:
            return currentNode
            
        elif value < currentNode.value and currentNode.left != None:
            return self.__find(currentNode.left,value)
            
        elif value > currentNode.value and currentNode.right != None:
            return self.__find(currentNode.right,value)        
        
    def delete(self,value):
        if self.root == None:
            print("Tree empty")
            
        elif self.search(value) == True:
            node = self.find(value)
            self.__deleteNode(node)
        
    def __deleteNode(self, currentNode):
        node1 = currentNode
        #define a function that finds the number of children for a current node
        def numOfChildren(node1):
            number = 0
            if node1.left != None:
                number = number+1
            if node1.right != None:
                number = number+1
            return number
                
        #define a function that finds the successor of a node in the tree
        def inorderSuccessor(node1):
            currNode = node1
            while currNode.left != None:
                currNode = currNode.left
                
            return currNode
        
        currNodeParent = currentNode.parent
        children = numOfChildren(currentNode)
        print("number of children node = ",children)
        #print("Parent of current node = ", currNodeParent.value)
        
        #case 1: If the node to be deleted is a leaf node, simply set the value of the current node to be None
        if children == 0:
            if currentNode != None:
                if currNodeParent.left == node1:
                    currNodeParent.left = None
            
                if currNodeParent.right == node1:
                    currNodeParent.right = None
        
        
        #case 2: If the node to be deleted has only one child, set the value of the currentNode as the value of that child node 
        #and value of child node to be None
        if children == 1:
            if currNodeParent != None:
                if currentNode == currNodeParent.left:
                    if currentNode.left == None:
                        currNodeParent.left = currentNode.right
                    else:
                        currNodeParent.left = currentNode.left
                if currentNode == currNodeParent.right:
                    if currentNode.right == None:
                        currNodeParent.right = currentNode.left
                    else:
                        currNodeParent.right = currentNode.right
                        
        #case 3: If the node has 2 children, find the inorder successor of the node and set the value of the inorder successor 
        #to the node to be deleted and set the value of inorder succesor node to be None
        if children == 2:
            successorNode = inorderSuccessor(currentNode)
            print("successor node = ", successorNode.value)
            currentNode.value = successorNode.value
            self.__deleteNode(successorNode)
            
class Node:
    def __init__(self,value):
        self.value  = value
        self.left   = None
        self.right  = None
        self.parent = None
        self.ht = 1 #Height of every leaf node is 1 and since every node is inserted as a leaf node, the height of that
                    #node will be one. Also, this would later in reflect the overall height of the tree.

BST1 = BinarySearchTree()
BST1.insert(5)
BST1.insert(10)
BST1.insert(1)
BST1.printTree()