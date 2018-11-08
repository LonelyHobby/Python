# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:32:12 2018

@author: DELL
"""

def delNum(s, k):
    n = len(s)
    if n<k: return None
    s = list(s)
    flag = 0
    while k != 0:
        if flag == 0:
            for i in range(len(s) - 1):  
                if s[i] < s[i + 1]:
                    del s[i]
                    k -= 1
                    flag = 1
                    break
        if flag == 1 and k != 0:  
            flag = 0
        else:  
            n = len(s)
            s = s[:n-k]
            k = 0
    return ''.join(s)

 

 

if __name__ == '__main__':

    s, k = '494326', 3

    print(delNum(s, k))