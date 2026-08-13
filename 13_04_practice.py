# 실습 1. 데이터 불러오기와 구조 확인하기

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv", encoding="utf-8")

# shape 확인
print(df.shape)  # (30, 7)

# columns의 열 이름 출력 확인
print(df.columns)
print(df.columns.tolist())
# ['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급']

# 실제 CSV파일 열어보고 shape, columns 그대로 나온건지 비교

# -----------------------------------------------------------------------------
# 실습 2. 열 선택하기

# data/13_diecasting_small.csv 파일 열기

# · 대괄호 한 겹으로 단일 열을 Series로 선택
# : '형체력' 컬럼 하나만 빼오기
s_force = df["형체력"]
print(type(s_force))
print(s_force.head())

# · 대괄호 두 겹으로 복수 열을 DataFrame으로 선택
# : '형체력', '실린더압력' 두개를 선택하기
df_two = df[["형체력", "실린더압력"]]
print(type(df_two))
print(df_two.head())

# · 선택한 열에 mean으로 평균 계산
print(round(df["형체력"].mean(), 1))  # 267.8

# -----------------------------------------------------------------------------
# 실습 3. 공정 센서 열 골라내기

# · 주조 로그 파일 불러오기
# data/13_diecasting_shot.csv 파일 열기
df_shot = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
print(df_shot.shape)  # (200, 7)

# · 한 센서 열을 Series로 선택
# '형체력' 선택
s_shot = df_shot["형체력"]
print(s_shot.head())

# · 여러 feature 열을 DataFrame으로 선택해 형태 확인
# df[['형체력', '실린더압력', '주조압력']].shape 출력
print(df_shot[["형체력", "실린더압력", "주조압력"]].shape)  # (200, 3)
