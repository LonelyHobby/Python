# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 19:55:40 2018

@author: DELL
"""

def merge_sort( li ):  
    if len(li) == 1:
        return li 
    mid = len(li) // 2    
    left = li[:mid]
    right = li[mid:]
    ll = merge_sort( left )
    rl =merge_sort( right )
    return merge(ll , rl)
def merge( left , right ):
    result = []
    while len(left)>0 and len(right)>0 :
        if left[0] <= right[0]:
            result.append( left.pop(0) )
        else:
            result.append( right.pop(0) )
    result += left
    result += right
    return result

if __name__ == '__main__':
    li = [5,4 ,3 ,2 ,1]
    li2 = merge_sort(li)
    print(li2)