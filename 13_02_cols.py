# 복수 열 선택

import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')
df.info()


df['형체력'].info() # Series
df[['형체력', '실린더압력']].info() # DataFrame
