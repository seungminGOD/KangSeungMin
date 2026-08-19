# 실습 5. 위험 순으로 정렬하기
# 데이터를 위험한 순서로 정렬하고 상위만 추출
import pandas as pd

df = pd.read_csv('data/13_diecasting_shot.csv', encoding='utf-8')
print(df.shape) # (200, 7)
df.info() # 비스킷두께 컬럼 발견!
print(df.head(3))

# · sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
# · head로 상위 다섯 개만 추출해 값 확인
print(df.sort_values("비스킷두께", ascending=False).head(5))

print("--------------------")

# · 여러 열을 리스트로 묶어 우선순위 다중 정렬
df_multi = df.sort_values(['품질등급', '형체력'], ascending=[True, False])
print(df_multi.head(5))

# 예상 결과
# 상위 5개 비스킷두께 값과 다중 정렬 첫 행 품질등급 출력