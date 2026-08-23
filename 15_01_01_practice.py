import pandas as pd

df_log = pd.read_csv('data/15_사출성형_로그.csv', encoding='utf-8')
print(df_log.describe())

# 실습 1. 눈으로 결측 찾기
# 설비 센서에서 진짜 결측과 위장 결측을 코드로 세기
# 진짜 결측(NaN)과 위장 결측을 코드로 세어 확인

# · 설비 센서 데이터를 불러와 isna로 컬럼별 NaN 개수 세기
print(df_log.isna().sum()) # True = 1, False = 0 합산
# 측정시각     0
# 사출기      1
# 배럴온도     2
# 사출압력     1
# 스크루속도    1
# 누적샷      0
# 불량여부     0

# · 조건 필터링으로 압력 0, 진동 -999 같은 위장 결측 개수 세기
print((df_log['사출압력'] == 0.0).sum()) # 2
print((df_log['스크루속도'] == -999.0).sum()) # 2

# · 진짜 결측과 위장 결측을 나눠 비교

# 예상 결과
# NaN 4개(온도2·압력1·진동1), 위장 압력0 2개·진동-999 2개