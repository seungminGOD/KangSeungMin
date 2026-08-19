# 실습 6. 필터링과 정렬 연결
# 조건으로 거른 결과에 정렬을 이어 붙이기
import pandas as pd

df = pd.read_csv('data/13_diecasting_shot.csv', encoding='utf-8')
df.info()
print(df.tail(5))

# · 고장 여부 조건으로 고장 설비만 먼저 거르기
# 품질등급 == 불량
df_bad = df[ df['품질등급'] == '불량' ]
print(len(df_bad)) # 20
print(df_bad.head())

# · 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬
# · head로 상위 다섯 개만 남겨 샷 확인
df_filtered = df[ df['품질등급'] == '불량' ].sort_values('비스킷두께', ascending=False).head(5)
print(df_filtered)

# 예상 결과
# 5개 행, 비스킷두께 큰 순 샷 목록 출력