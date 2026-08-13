# loc 행과 열

import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')
df.info()

print("-" * 40)

s = df.loc[0]
s.info() # Series

# 행(row) 언급 서브 DF 만들기
df_sub = df.loc[0:2] # DataFrame
df_sub.info()
print(df_sub)

# 행(row)과 열(col) 언급 서브 DF 만들기
df_sub2 = df.loc[0:2, ['품질등급', '형체력']]
df_sub2.info()
print(df_sub2)