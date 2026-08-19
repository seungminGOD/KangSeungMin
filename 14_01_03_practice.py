# 실습 1. value_counts로 빈도 세기
# 한 열을 골라 value_counts로 값별 개수 세기
# 한 열의 값별 개수를 세어 데이터 구성 파악
import pandas as pd

df = pd.read_csv('data/14_hydraulic.csv', encoding='utf-8')
df.info()
print(df.head(3))

# · 설비 데이터를 불러와 앞부분과 구조 확인
# · 설비 열(컬럼)에 value_counts를 붙여 값별 개수 세기
print(df['밸브상태'].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19

# · 교대 열도 같은 방법으로 세어 가장 많은 값 확인
print(df['운전부하'].value_counts())
# 운전부하
# 고부하    60
# 저부하    60

# 예상 결과
# 설비별·교대별 빈도표 출력 (심각 42건이 최다) x

print("--------------------------------------")

# 실습 2. 비율과 불균형 데이터
# qc 합격·불합격 빈도와 비율로 불균형 확인
# 합격·불합격 빈도와 비율을 구해 불균형 데이터 확인
df_qc = pd.read_csv('data/14_hydraulic_qc.csv', encoding='utf-8')
df_qc.info()
print(df_qc.head(3))

# · 공정 데이터의 판정 열에 value_counts로 합격·불합격 개수 세기
print(df_qc['검사결과'].value_counts())
# 검사결과
# 합격     188
# 불합격     12

# · normalize 옵션으로 각 값의 비율을 소수로 확인
print(df_qc['검사결과'].value_counts(normalize=True))
# 검사결과
# 합격     0.94
# 불합격    0.06

# · round로 비율을 소수점 셋째 자리까지 정리
print(df_qc['검사결과'].value_counts(normalize=True).round(1))
# 검사결과
# 합격     0.9
# 불합격    0.1

# 예상 결과
# 불합격이 전체 약 6%인 불균형 확인