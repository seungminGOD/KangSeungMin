# 실습 1. head·tail로 디지털 신호 살펴보기
import pandas as pd

df = pd.read_csv("data/12_metro_digital.csv", encoding="utf-8")

# 위 코드가 정상 실행되어 shape가 나오는지 부터 확인 후
print(df.shape)  # (120, 4)

# 적절한 숫자들의 줄을 정해 .head()와 .tail() 출력
print(df.head(5))
print(df.tail(3))

# head와 tail 출력에서 NaN 위치가 보이는지도 확인
print(df.isna().sum())


# 실습 2. head·tail 행 개수 조절
# 숫자 인자를 바꿔가며 원하는 만큼 보는 감각 익히기

df_sensor = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")
print(df_sensor.shape)  # (200, 7)

# STEP 1 — head(1) · head(10) · tail(7) · head(500) 출력 비교
print("--- head(1) ---")
print(df_sensor.head(1))  # 1줄

print("--- head(10) ---")
print(df_sensor.head(10))  # 10줄

print("--- tail(7) ---")
print(df_sensor.tail(7))  # 7줄

print("--- head(500) ---")
print(df_sensor.head(500))  # 오류 없이 200줄(전체)만 출력

# 1) head(1)은 1줄, head(10)은 10줄 — 숫자대로 출력
# 2) head(500)도 오류 없이 있는 만큼만 나옴
# 3) 앞 3줄: head(3), 뒤 3줄: tail(3)
print(df_sensor.head(3))
print(df_sensor.tail(3))
