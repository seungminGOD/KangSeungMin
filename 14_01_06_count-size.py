
import pandas as pd

# 어제까지 배운 groupby 다시 살펴보기
df = pd.read_csv('data/14_hydraulic.csv', encoding='utf-8')

# groupby로 냉각기상태마다 평균 온도 - 소숫점이하 2자리
print(df.groupby('냉각기상태')['온도'].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89

# groupby로 운전부하마다 평균 진동 - 소숫점이하 3자리
print(df.groupby('운전부하')['진동'].mean().round(3))
# 운전부하
# 고부하    0.602
# 저부하    0.629

# 냉각기상태별로 다시 운전부하별 그룹을 나누어 평균 온도 
print(df.groupby(['냉각기상태', '운전부하'])['온도'].mean().round(2))
# 냉각기상태  운전부하
# 고장     고부하     55.51
#        저부하     54.05
# 저하     고부하     44.07
#        저부하     45.58
# 정상     고부하     35.89

# 냉각기상태별로 얼마나 많은 항목이 있을까?
print(len(df[df['냉각기상태'] == '고장'])) # 40
# 위 코드처럼 각 상태별로 갯수를 따로따로 계산하는 것은 비효율적 - size 활용
print(df.groupby('냉각기상태').size())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40