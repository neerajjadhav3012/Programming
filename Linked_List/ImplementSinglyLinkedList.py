
# coding: utf-8

# # Implement a Singly Linked List
# 
# For this interview problem, create a node class and show how it can be used to create a Singly Linked List

# In[2]:

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    


# In[26]:

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insertAtBeginning(self, data):
        self.size +=1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            newNode.nextNode = None
        
        else:
            newNode.nextNode = self.head
            self.head = newNode
            
    def insertAtEnd(self, data):
        self.size +=1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode:
            actualNode = actualNode.nextNode
            
        actualNode.nextNode = newNode
        
    def traverse(self):
        actualNode = self.head
        while actualNode:
            print(actualNode.data)
            actualNode = actualNode.nextNode
            
    def remove(self, dat):
        if self.head is None:
            return 
        
        self.size -=1
        previousNode = None
        currentNode = self.head
        
        while currentNode.data != dat:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
        
    


# In[28]:

l = LinkedList()
l.insertAtBeginning(1)
l.insertAtEnd(2)
l.insertAtBeginning(100)
l.insertAtEnd(22)
l.remove(2)
l.remove(1)
l.traverse()


# 

# In[ ]:



