#coding=utf-8
# python set


x = [1, 2, 3, 4]
y = [1, 3, 6, 9]


## 交集
print(set(x) & set(y))

## 差集
print(set(x) - set(y))

## 并集
print(set(x) | set(y))

## out
"""
set([1, 3])
set([2, 4])
set([1, 2, 3, 4, 6, 9])
"""