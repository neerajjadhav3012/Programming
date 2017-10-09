
# coding: utf-8

# # Sentence Reversal
# 
# ## Problem
# 
# Given a string of words, reverse all the words. For example:
# 
# Given:
#     
#     'This is the best'
# 
# Return:
# 
#     'best the is This'
# 
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
# 
#     '  space here'  and 'space here      '
# 
# both become:
# 
#     'here space'
# 
# ## Solution
# 
# Fill out your solution below:

# In[19]:

def rev_word(s):
    words = s.strip().split()
    words.reverse()
    return " ".join(words)
      


# In[20]:

rev_word('Hi John,   are you ready to go?')


# In[21]:

rev_word('    space before')


# _____

# # Test Solution

# In[22]:

"""
RUNNIG THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)


# ## Good Job!
