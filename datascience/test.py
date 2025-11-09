import pandas as pd

df = pd.DataFrame()

A = [1,2,3,4,5]
B = ["a",2,3,4,5]

df["A"] = A
df["B"] = B
df = df[df["A"]!=2]
df.loc[df["B"] == "a",'B']=4

df.loc[df["A"]<=3,"A"] = 42
df=df.reset_index()
df=df.drop(columns="index")
print("df")
print(df)

df2 = df[(df["A"] == 42) & (df["B"]==3)]
print("df2")
print(df2)

df3 = pd.concat([df,df2],ignore_index=True)
df4 = pd.merge(left=df,right=df3,how="inner",on="A")

print("df3")
print(df3)
print("df4")
print(df4)
