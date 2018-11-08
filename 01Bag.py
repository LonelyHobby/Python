# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:49:37 2018

@author: DELL
"""

memo={}
def maxVal(w, v, i, ws):
    try:
        return memo[(i,ws)]
    except KeyError:
        if i == 0:
            if w[i] <= ws:
                memo[(i, ws)] = v[i]
                return v[i]
            else:
                memo[(i, ws)] = 0
                return 0
        without_i = maxVal(w, v, i-1, ws)
        if w[i] > ws:
            memo[(i, ws)] = without_i
            return without_i
        else:
            with_i = maxVal(w, v, i-1, ws-w[i]) + v[i]
        res = max(without_i, with_i)
        memo[(i, ws)] = res
        return res

w = [5, 3, 2]
v = [9, 7, 8]
val = maxVal(w, v, 2, 5)
print(val)


n = 3      # 物品数量
c = 30      # 包的载重量
w = [20, 15, 15] # 物品重量
v = [45, 25, 25] # 物品价值
maxw = 0 # 合条件的能装载的最大重量
maxv = 0 # 合条件的能装载的最大价值
bag = [0,0,0] # 一个解（n元0-1数组）长度固定为n
bags = []   # 一组解
bestbag = None # 最佳解
def conflict(k):
  global bag, w, c
  # bag内的前k个物品已超重，则冲突
  if sum([y[0] for y in filter(lambda x:x[1]==1, zip(w[:k+1], bag[:k+1]))]) > c:
    return True
  return False
# 套用子集树模板
def backpack(k): # 到达第k个物品
  global bag, maxv, maxw, bestbag
  if k==n: # 超出最后一个物品，判断结果是否最优
    cv = get_a_pack_value(bag)
    cw = get_a_pack_weight(bag)
    if cv > maxv : # 价值大的优先
      maxv = cv
      bestbag = bag[:]
    if cv == maxv and cw < maxw: # 价值相同，重量轻的优先
      maxw = cw
      bestbag = bag[:]
  else:
    for i in [1,0]: # 遍历两种状态 [选取1, 不选取0]
      bag[k] = i # 因为解的长度是固定的
      if not conflict(k): # 剪枝
        backpack(k+1)
# 根据一个解bag，计算重量
def get_a_pack_weight(bag):
  global w
  return sum([y[0] for y in filter(lambda x:x[1]==1, zip(w, bag))])
# 根据一个解bag，计算价值
def get_a_pack_value(bag):
  global v
  return sum([y[0] for y in filter(lambda x:x[1]==1, zip(v, bag))])
# 测试
backpack(0)
print(bestbag, get_a_pack_value(bestbag))