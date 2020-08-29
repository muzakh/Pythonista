'''
Author: Zohaib
Date: 24th Aug 2020
Description: Tree Traversal Algorithms: 
             1.  InOrder Tree Traversal Algorithm (leftchild --> Root --> RightChild)


    
      1  
   2     3
4     5


'''

class Node:
    def __init__(self, value):
        self.leftchild = None
        self.rightchild = None
        self.nodevalue = value
    
root = Node(1)
root.leftchild = Node(2)
root.rightchild = Node(3)
root.leftchild.leftchild = Node(4) 
root.leftchild.rightchild = Node(5) 

def InOrder(root):
    if root:
        InOrder(root.leftchild)
        print(root.nodevalue)
        InOrder(root.rightchild)
        
InOrder(root)


'''
Result:
=======

4
2
5
1
3

'''
