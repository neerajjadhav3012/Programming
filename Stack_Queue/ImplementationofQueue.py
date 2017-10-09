
# coding: utf-8

# # Implementation of Queue
# 
# In this lecture we will build on our previous understanding of Queues by implementing our own class of Queue!

# ____
# ## Queue Methods and Attributes
# 
# 
# Before we begin implementing our own queue, let's review the attribute and methods it will have:
# 
# * Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
# * enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
# * dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
# * isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
# * size() returns the number of items in the queue. It needs no parameters and returns an integer.

# ____
# ## Queue Implementation

# In[8]:

class Queue(object):
    
    def __init__(self):
        self.ele = []
        
    def isEmpty(self):
        return len(self.ele) == 0
    
    def size(self):
        return len(self.ele)
    
    def enqueue(self, item):
        return self.ele.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.ele.pop(0)
        else:
            return("The Queue is Empty")
    


# In[9]:

q = Queue()


# In[10]:

q.size()


# In[11]:

q.isEmpty()


# In[12]:

q.enqueue(1)


# In[13]:

q.dequeue()


# 

# In[14]:

q.dequeue()


# In[ ]:



