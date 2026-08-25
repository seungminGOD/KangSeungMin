import pandas as pd

df = pd.read_csv('data/16_diecasting.csv', encoding='utf-8')

# 실습 4. 평균·중앙값으로 이상치 영향 확인
# 이상치가 평균을 끌어당기는 정도를 중앙값과 비교

# · 사이클타임의 평균과 중앙값을 각각 구해 차이 확인 -> mean, median
print(df['사이클타임'].mean()) # 64.75
print(df['사이클타임'].median()) # 22.6

print(df['사이클타임'].agg(['mean', 'median']))
# mean      64.75
# median    22.60

# · 상태가 정상인 행만 조건으로 골라내기 (상태: 0 정상, 1 문제있음)
df_ok = df[ df['상태'] == 0 ]

# · 정상만의 평균이 중앙값에 가까워지는지 확인 (정상만의 평균을 출력해서 전체의 중앙값과 비교)
print(df_ok['사이클타임'].mean().round(2)) # 27.67

# 예상 결과
# 평균 64.75 vs 중앙값 22.6, 정상만 평균 27.67