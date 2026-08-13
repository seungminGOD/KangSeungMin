# 단일 컬럼(col) 선택

import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')
df.info()

# 데이터 프레임(2차원)에서 컬럼 한개를 도려내보면 시리즈(1차원)가 된다
s = df['형체력'] 
s.info()