import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')

# 실습 6. 최빈값·앞뒤 값 대체
# 범주형은 최빈값, 시계열은 앞뒤 값으로 채우기

# · 범주형 열의 최빈값을 구해 채우기
# 사출기 컬럼은 1혹기~3호기 범주형으로 판단
print(df['사출기'].isna().sum()) # 억지로 3개 만들어봤어요!
print(df['사출기'].mode()[0]) # 1호기가 가장 많다고 함

df['사출기'] = df['사출기'].fillna(df['사출기'].mode()[0])
print(df['사출기'].isna().sum()) # 다시 채워서 0개!

# · 측정시각 순으로 정렬해 시계열 순서 만들기
df = df.sort_values('측정시각')

# · ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기
print(df['전환압력'].isna().sum()) # 68개 NaN 확인
df['전환압력'] = df['전환압력'].ffill().bfill() # 자주 볼 시계열 채우기 패턴
print(df['전환압력'].isna().sum()) # 0개 NaN 확인

# 예상 결과
# 설비명은 최빈값(절삭기A), 온도는 앞뒤 값으로 대체

print("--------------------------------")
# 실습 7. 그룹별 대체
# 그룹별 평균으로 채워 집단 특성 반영

# · 제품유형으로 그룹을 나누기
print(df.groupby('사출기')['감압시간'].mean())
# 사출기별로 감압시간 평균이 다른 것 확인
# 1호기    0.322179
# 2호기    0.322368
# 3호기    0.322400

# · 각 그룹의 평균으로 그 그룹의 결측을 채우기

# 사출기별로 그룹을 나누고
# 그룹마다 갑압시간의 시리즈를 뽑아서
# 그 시리즈의 NaN들을 그 시리즈의 평균들로 채운다
df['감압시간'] = df.groupby('사출기')['감압시간'].transform(
    lambda s: s.fillna(s.mean())
)

print(df['감압시간'].isna().sum()) # 0

# · 남은 수치 결측은 전체 중앙값으로 마무리하고 검증
# 이런 코드는 실제로 할 가능성이 전혀 없음 - 컬럼의 특성고려 없이 NaN을 다 채운다?
df_numbers = df.select_dtypes('number')
df[df_numbers.columns] = df_numbers.fillna(df_numbers.median())

print(df.isna().sum())
print(df.isna().sum().sum())

# 예상 결과
# 토크를 유형별 평균으로 대체, 남은 결측 0