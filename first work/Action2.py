# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:50:00 2021

@author: songqianqian
"""


import pandas as pd
data= {'语文': [68,95,98,90,80],
        '数学': [65,76,86,88,90], 
        '英语': [30,98,88,77,90]}
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data, index=['张飞','关羽','刘备','典韦','许褚'])
print(df1)
print(df2)
#平均值
print(df2.mean())
#最小值
print(df2.min())
#最大值
print(df2.max())
#方差
print(df2.var())
#标准差
print(df2.std())
#总成绩
print(df2.sum(axis=1))
#添加总成绩列
df2['总成绩']=df2.apply(lambda i:i.sum(),axis=1)
#输出降序排列
print(df2.sort_values('总成绩',ascending=False))





