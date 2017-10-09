
# coding: utf-8

# # Implementation of Deque
# 
# In this lecture we will implement our own Deque class!
# 
# ## Methods and Attributes
# 
# * Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
# * addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
# * addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
# * removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
# * removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
# * isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
# * size() returns the number of items in the deque. It needs no parameters and returns an integer.
# 
# ## Deque Implementation

# In[43]:

class Deque(object):
    
    def __init__(self):
        self.ele = []
        
    def isEmpty(self):
        return len(self.ele) == 0
    
    def size(self):
        return len(self.ele)
    
    def addFront(self,item):
        self.ele.insert(0,item)
    
    def addRear(self, item):
        self.ele.append(item)
        
    def removeFront(self):
        if not self.isEmpty():
            return self.ele.pop(0)
        else:
            return("Deque is empty")
    
    def removeRear(self):
        if not self.isEmpty():
            return self.ele.pop()
        else:
            return("Deque is empty")


# In[44]:

d = Deque()


# In[45]:

d.addFront('hello')


# In[46]:

d.addRear('world')


# In[47]:

d.size()


# In[48]:

print(d.removeFront() + ' ' +  d.removeRear())


# In[49]:

d.size()


# 

# In[ ]:



