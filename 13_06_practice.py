# 실습 4. loc와 iloc로 행 선택하기
# 라벨 기준 loc와 번호 기준 iloc로 행 선택, 범위 차이 확인
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv", encoding="utf-8")

# · loc로 라벨 기준 단일 행 선택
print(df.loc[0, "품질등급"])  # 양품

# · iloc로 번호 기준 단일 행 선택
# df.iloc[0] -> 특정 row number인 row의 Serise 추출
# ..['품질등급'] -> 해당 Serise에서 '품질등급' 컬럼의 내용만 추출
print(df.iloc[0]["품질등급"])  # 양품

# · 범위 선택으로 loc 끝 포함·iloc 끝 제외 차이 확인
# loc[0:2] -> 3행 (0, 1, 2) — 끝 라벨 포함
# iloc[0:2] -> 2행 (0, 1) — 끝 위치 제외
# 두 결과는 다름
print(len(df.loc[0:2]))  # 3
print(len(df.iloc[0:2]))  # 2

# -------------------------------------------------
# 실습 5. loc·iloc로 행·열 동시 선택하기
# 행과 열을 동시에 지정해 원하는 부분만 추출

# data/13_diecasting_small.csv 사용

# · loc로 행 범위와 열 이름을 함께 지정
df_sub = df.loc[0:4, ["품질등급", "형체력"]]
print(df_sub.shape)  # (5, 2)

# · 다른 행 범위에서 세 열 선택
df_sub2 = df.loc[10:14, ["형체력", "실린더압력", "주조압력"]]
print(df_sub2.shape)  # (5, 3)

# · iloc 음수 인덱스로 마지막 행 선택
print(len(df.iloc[-3:]))  # 3

# -------------------------------------------------
# 실습 6. 특정 구간 추출 종합
# 열 선택·loc·iloc를 결합해 특정 구간을 추출하는 종합
df_shot = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")

# · 여러 feature 열을 선택한 뒤 iloc로 앞 구간 추출
cols = ["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]
print(df_shot[cols].iloc[0:10].shape)  # (10, 5)

# · loc 라벨 범위로 두 열 구간 추출
cols2 = ["실린더압력", "주조압력"]
print(df_shot.loc[0:9, cols2].shape)  # (10, 2)

# · iloc 위치 범위로 앞쪽 열 구간 추출
print(df_shot.iloc[50:60, 0:6].shape)  # (10, 6)
