'''
Author: Zohaib
Date: 24th Aug 2020
Description: Tree Traversal Algorithms: 
             1.  PreOrder Tree Traversal Algorithm (Root --> leftchild --> RightChild   OR  /__)


    
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

def PreOrder(root):
    if root:
        print(root.nodevalue)
        PreOrder(root.leftchild)
        PreOrder(root.rightchild)
        
PreOrder(root)


'''
Result:
=======

1
2
4
5
3
'''
