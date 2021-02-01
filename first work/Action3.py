


import pandas as pd

#数据加载
df = pd.read_csv('car_complain.csv')
print(df)

#拆分problem类型 => 多个字段
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
print(df)

#数据清洗,将别名合并
def f(s):
    s=s.replace('一汽-大众','一汽大众')
    return s
df['brand']=df['brand'].apply(f)

#品牌投诉总数
result1=df.groupby(['brand'])['id'].agg(['count'])
print(result1)

#车型投诉总数
result2=df.groupby(['car_model'])['id'].agg(['count'])
print(result2)

#哪个品牌的平均车型投诉最多
result3=df.groupby(['brand','car_model'])['id'].agg(['count'])
result3=result3.sort_values('count',ascending=False)
print(result3)



