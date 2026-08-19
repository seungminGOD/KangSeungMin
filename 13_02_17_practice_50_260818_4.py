# 실습 7. 이상 의심 설비 리포트
# 불러오기부터 판단 문장까지 전체 워크플로우를 두 데이터에 적용
import pandas as pd

# 분석 워크플로우 5단계 맞춰가기
# 1. 불러오기
df = pd.read_csv('data/13_diecasting_shot.csv', encoding='utf-8')

# 2. 확인하기
df.info()

# 3. 필터링
df_warning = df[ (df['비스킷두께'] >= 16) | (df['사이클타임'] >= 100) ]
print(len(df_warning)) # 76
# 4. 정렬
df_report = df_warning.sort_values('비스킷두께', ascending=False)
print(df_report.head())

# 5. 선택 : [[...]] 대괄호 중첩 주의!!
df_final = df_report[['샷', '품질등급', '형체력', '사이클타임']]

print("-------------------")
print("가장 위험 목록")
print(df_final.head())

df_danger = df_final.head(1)
print("가장 위험한 항목")
print(df_danger)

# · 복합 조건으로 위험 설비를 거르고 비스킷두께 내림차순 정렬
# · 필요한 주요 열만 선택하고 가장 위험한 설비로 판단 문장 작성
# · 같은 흐름을 주조 로그 불량 데이터에도 적용해 결과 비교

# 예상 결과
# 주조 로그 위험 50건·판단 문장, 주조 로그 불량 상위 목록 출력