
# coding: utf-8

# # Implementation of Stack
# 
# ## Stack Attributes and Methods
# 
# Before we implement our own Stack class, let's review the properties and methods of a Stack.
# 
# The stack abstract data type is defined by the following structure and operations. A stack is structured, as described above, as an ordered collection of items where items are added to and removed from the end called the “top.” Stacks are ordered LIFO. The stack operations are given below.
# 
# * Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
# * push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
# * pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
# * peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
# * isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
# * size() returns the number of items on the stack. It needs no parameters and returns an integer.

# ____
# 
# ## Stack Implementation

# In[57]:

class Stack(object):
    
    def __init__(self):
        self.ele = []
    
    def push(self, item):
        self.ele.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.ele.pop()
        else:
            return("Stack is Empty")
    
    def peek(self):
        return self.ele[-1]
    
    def isEmpty(self):
        return len(self.ele) == 0
    
    def size(self):
        return len(self.ele)
        
    


# Let's try it out!

# In[58]:

s = Stack()


# In[59]:

print(s.isEmpty())


# In[60]:

s.push(1)


# In[61]:

s.push('two')


# In[62]:

s.peek()


# In[63]:

s.push(True)


# In[64]:

s.size()


# In[65]:

s.isEmpty()


# In[66]:

s.pop()


# In[67]:

s.pop()


# In[68]:

s.size()


# In[69]:

s.pop()


# In[70]:

s.isEmpty()


# 

# In[71]:

s.pop()


# In[ ]:



