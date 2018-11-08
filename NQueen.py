# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 23:47:02 2018

@author: DELL
"""


def nQueens(n, x=0, *solution): 
    if x == n: 
        yield solution 
    else: 
        for y in range(n): 
            if all(y != j and abs(x - i) != abs(y - j) for i, j in solution): 
                yield from nQueens(n, x + 1, *solution, (x, y))    
if __name__ == '__main__': 
    fp= open("f:\\Source\\Python\\Result.txt", "wt") 
    def showSolution(solutions, n): 
        for i, s in enumerate(solutions, 1): 
            print("%s:\n" % i + "=" * 20,file=fp)   
            for x in range(n): 
                for y in range(n):                  
                        print('Q ' if s[x][1] == y else '_ ', end='',file=fp)
                print(" ",file=fp)
            print(" ",file=fp)
            fp.flush()
    
N = 8 
showSolution(nQueens(N), N)