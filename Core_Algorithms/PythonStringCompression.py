
# coding: utf-8

# # String Compression
# 
# ## Problem
# 
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 
# 
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

# ## Solution
# Fill out your solution below:

# In[19]:

def compress(s):
    
    if len(s) == 0:
        return ""
    
    if len(s) == 1:
        return s[0] + "1"
    
    output = ""
    count = 1
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            count+=1
        else:
            output+=s[i-1] + str(count)
            count = 1
            
    output+=s[i] + str(count)
    return output


# In[20]:

compress('A')


# # Test Solution

# In[21]:

"""
RUNNIG THIS CELL TO TEST SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print("ALL TEST CASES PASSED")

# Run Tests
t = TestCompress()
t.test(compress)


# 

# In[ ]:



