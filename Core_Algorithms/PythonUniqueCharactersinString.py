
# coding: utf-8

# # Unique Characters in String
# 
# ## Problem
# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

# ## Solution
# Fill out your solution below:

# In[2]:

def uni_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 1
        else:
            return False
    return True


# # Test Solution

# In[4]:

"""
RUNNIG THIS CELL TO TEST CODE
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)


# 

# In[ ]:



