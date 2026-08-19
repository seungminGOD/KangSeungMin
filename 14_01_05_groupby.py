# groupby 기본 코드

import pandas as pd

df = pd.read_csv('data/14_hydraulic.csv', encoding='utf-8')
df.info()
print(df.head(3))

# '냉각기상태' 컬럼의 내용별로 그룹핑을 하자 -> 분할
# 분할된 DF마다 '온도' 컬럼이 있으니까, '온도'의 평균을 구해보자.
print(df.groupby('냉각기상태')['온도'].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89

# 온도 말고 냉각기상태별 진동 평균도 알고 싶다면?
print(df.groupby('냉각기상태')['진동'].mean().round(2))
# 냉각기상태
# 고장    0.69
# 저하    0.61
# 정상    0.55

# 냉각기상태에 따른 그룹별 온도 평균과 진동 평균
print(df.groupby('냉각기상태')[['온도', '진동']].mean().round(2))
#           온도    진동
# 냉각기상태             
# 고장     54.67  0.69
# 저하     45.46  0.61
# 정상     35.89  0.55