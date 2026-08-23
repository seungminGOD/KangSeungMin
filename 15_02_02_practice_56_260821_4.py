import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
df.info()

# 실습 1. dropna로 행·열 삭제
# 결측 있는 행과 열을 삭제하고 크기 변화 확인
# 결측 있는 행과 열을 삭제하고 크기 변화 확인

# · 원본 크기를 shape로 확인
print(df.shape) # (250, 22)

# · dropna로 결측 있는 행을 모두 삭제
print(df.dropna().shape) # (76, 22)

# · 방향을 열로 바꿔 결측 있는 열을 삭제
print(df.dropna(axis = 1).shape) # (250, 10)

# 예상 결과
# 250×22 → 행삭제 76×22, 열삭제 250×10

print('-------------------------------')

# 실습 2. dropna 옵션 조절
# how·thresh·subset로 삭제 기준을 세밀하게 조절

# · how로 완전히 빈 행만 삭제하는 기준 적용 -> how = 'all'
print(df.dropna(how = 'all').shape) # (250, 22)
# 250개 row가 다 살아남았다는 의미 
# : NaN으로 모든 컬럼 내용이 다 채워진 row가 없다는 뜻

# · thresh로 값이 일정(예, 20개) 개수 "이상"인 행만 남기기 -> thresh = 20
print(df.dropna(thresh = 20).shape) # (162, 22)
# 250 - 162 = 88개 row는 NaN이 3개 이상이라는 뜻

# · subset으로 특정 컬럼이 빈 행만 삭제
# 예, 불량여부 컬럼에 NaN이 있는 row들만 제거 -> subset = ['불량여부']
print(df.dropna(subset = ['불량여부']).shape) # (250, 22)
# '불량여부' 컬럼에는 NaN이 하나도 없다고 판단 가능

# 예상 결과
# 완전 결측 행만 삭제는 거의 유지, 임계값 20은 162행