
# coding: utf-8

# # Balanced Parentheses Check 
# 
# ## Problem Statement
# 
# Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. 
# 
# 
# You can assume the input string has no spaces.
# 
# ## Solution
# 
# Fill out your solution below:

# In[15]:

def balance_check(s):
    starting = ("[", "{", "(")
    pairs = [("[","]"), ("{","}"), ("(", ")") ]
    
    seen = []
    for char in s:
        if char in starting:
            seen.append(char)
        else:
            
            if seen == []:
                return False
            
            if (seen.pop(), char) not in pairs:
                return False
    
    return len(seen) == 0
    


# In[16]:

balance_check('[]')


# In[17]:

balance_check('[](){([[[]]])}')


# In[18]:

balance_check('[](){([[[]]])}(')


# # Test Solution

# In[19]:

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print("ALL TEST CASES PASSED")
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)


# 
