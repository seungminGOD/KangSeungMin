import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
print(df.shape) # (250, 22)
print(df.isna().sum())

# 실습 3. 결측 비율 기준 컬럼 제거
# 결측 비율이 높은 컬럼만 골라 제거

# 단계
# · 컬럼별 결측 비율을 계산
df_rate = df.isna().sum() / len(df)
print(df_rate)

# · 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기 
# -> 40% 이상 NaN으로 채워진 컬럼 목록
df_terminates = df_rate[df_rate > 0.4]
print(df_terminates)

# 최초 컬럼 이름들이 df_terminates의 index labels가 되었다.
list_terminates = df_terminates.index.tolist() # ['최대사출속도', '감압시간']
print(list_terminates)

# · 그 컬럼들을 drop으로 제거하고 크기 확인
# drop에 컬럼을 제시하면 기본동작 : 컬럼을 지워버림
df_final = df.drop(columns = list_terminates)
df_final.info()

# 예상 결과
# 40% 초과 센서19·20 제거 → 250×20

print("--------------------------------------")

# 실습 4. 삭제 손실 비교
# 삭제 방식별 남는 행 수와 손실률을 표로 비교

# 단계
# · 원본·행삭제·thresh 각 방식의 남는 행 수 구하기
# · 방식과 행 수를 하나의 표로 모으기

비교 = pd.DataFrame({
    '방식': ['원본', '행삭제', 'thresh20'],
    '행': [len(df), len(df.dropna()), len(df.dropna(thresh = 20))]
})

비교['손실률'] = ((1 - 비교['행'] / len(df)) * 100) .round(2)

print(비교)
#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2

# 위 코드는 너무 고급기술 - DF의 더 깊은 이해 경험 필요
# 여러분은 그냥 개별 3가지 항목들을 따로따로 계산시켜 출력해도 괜찮아요


# · 원본 대비 손실률을 백분율로 계산해 나란히 보기

# 예상 결과
# 행삭제 손실 약 70%, thresh 손실 약 35%