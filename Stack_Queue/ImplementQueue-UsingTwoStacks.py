
# coding: utf-8

# # Implement a Queue - Using Two Stacks
# 
# Given the Stack class below, implement a Queue class using **two** stacks! Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.

# In[1]:

# Uses lists instead of your own Stack class.
stack1 = []
stack2 = []


# ## Solution
# 
# solution below:

# In[2]:

class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.append(element) 
        
       
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1: 
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


# # Test Solution
# 
# You should be able to tell with your current knowledge of Stacks and Queues if this is working as it should. For example, the following should print as such:

# In[4]:

"""
RUNNIG THIS CELL TO CHECK IF THE SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())


# 

# In[ ]:



