
# coding: utf-8

# # Anagram Check
# 
# ## Problem
# 
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 
# 
# For example:
# 
#     "public relations" is an anagram of "crap built on lies."
#     
#     "clint eastwood" is an anagram of "old west action"
#     
# **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
# 
# ## Solution
# 
# Fill out your solution below:

# In[10]:

def anagram(s1,s2):
    
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    
    counter = {}
    for char in  s1:
        if char in counter:
            counter[char] +=1
        else:
            counter[char] = 1
            
    for char in s2:
        if char in counter:
            counter[char] -=1
        else:
            return False
    
    for chars in counter:
        if counter[char] !=0:
            return False
    return True


# In[11]:

anagram('dog','god')


# In[12]:

anagram('clint eastwood','old west action')


# In[13]:

anagram('aa','bb')


# # Test Your Solution
# Run the cell below to test your solution

# In[14]:

"""
RUNNIG THIS CELL TO TEST SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)


# In[ ]:




# 
