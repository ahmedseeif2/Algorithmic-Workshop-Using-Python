#!/usr/bin/env python
# coding: utf-8

# In[2]:


### First, determines whether a subsequence exists


# In[8]:


def verify_subseq(seq, subseq):
    it = iter(seq)
    for ch in subseq:      
        if ch not in it:    
            return False    

    return True , len(subseq)   


# In[19]:


verify_subseq([1,2,4,8,9], [1,2,4])


# In[ ]:


### Then determines if a subsequence is increasing by comparing each item to its next successor


# In[17]:


def verify_increasing(seq):
    if not seq:         
        return True

    seq = [character for character in seq]    # convert to a list
    comp_seq = seq[1:]          # make separate list without first item
    seq.pop()                   # remove last item from original list

    # True if every item is less than than its successor
    result = all(j < k for j, k in zip(seq, comp_seq))

    return result


# In[18]:


verify_increasing([1,2,4,8,9,5,13,8])


# In[ ]:





# In[30]:


def longest_increasing_subsequence(X):
    
    N = len(X)
    P = [0] * N
    M = [0] * (N+1) 
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo+hi)//2
            if (X[M[mid]] < X[i]):
                lo = mid+1
            else:
                hi = mid-1
 
        newL = lo
        P[i] = M[newL-1]                                               
        M[newL] = i
      
       
        if (newL > L):
            L = newL
    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(X[k])
        k = P[k]
       
       

   
    return S[::-1], len(S)


# In[31]:


longest_increasing_subsequence([1,2,4,8,9,5,65,23,89,14,26,786,652])

