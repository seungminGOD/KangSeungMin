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


# 실습 3. 구조 파악 3중 도구
# shape colums dtypes로 데이터 뼈대 읽기

# 12_metro_digital.csv 읽어와서 dataframe에 담기
df_digital = pd.read_csv("data/12_metro_digital.csv", encoding="utf-8")

# .shape 출력
print(df_digital.shape)  # (120, 4)

# .columns 출력 df.columns.tolist()도 출력
print(df_digital.columns)
print(df_digital.columns.tolist())  # ['측정시각', '압축기', '타워', '저압스위치']

# .dtypes 출력
print(df_digital.dtypes)

# 실습 4. 열 이름 자료형 점검

# 12_metro_compressor.csv 읽어와서 DF에 담기
df_compressor = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")

# .columns 출력 df.columns.tolist()도 출력
print(df_compressor.columns)
print(df_compressor.columns.tolist())
# ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']

print(df_compressor.dtypes)

# 실습 5. info로 데이터 건강검진

# 12_metro_digital.csv 파일을 읽어서 DF 생성
df_info = pd.read_csv("data/12_metro_digital.csv", encoding="utf-8")

# DF의 info() 호출 출력
df_info.info()

# -----------------------------------------------------------------------------
# 실습 6. describe로 이상 신호 찾기
# 평균/분위수/최대를 읽어 이상 신호 있는 열 찾기
#
# - df.describe() 결과를 가로질러 읽으며 이상치(Outlier) 신호를 탐지합니다.
# - ★ 이상 탐지 핵심 노하우: 75% 분위수 지점과 max(최댓값) 수치의 거리를 비교합니다!
#   * 75% 지점 수치와 max 수치가 가깝다 -> 값이 고르게 분포한 정상 상태
#   * 75% 지점 수치와 max 수치의 간격이 지나치게 멀다 -> 상위 극단치가 존재하는 이상 과열 신호! (추가 조사 필요)
# -----------------------------------------------------------------------------

# 12_metro_compressor.csv
df_desc = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")
print(df_desc.shape)  # (200, 7)

df_desc.info()

# STEP1 : describe 후 75%와 max 차이 큰 열 찾기
desc = df_desc.describe()
print(desc)
print(desc.loc["max"] - desc.loc["75%"])

# 1 온도의 평균과 최댓값 차이를 숫자로 적었는가
# 평균 63.18℃ 대 max 75.0℃ — 차이 11.82
# 75.000000 - 63.181910 = 11.818090

# 2 75%와 max 차이가 큰 열을 두 개 이상 찾았는가
# 오일온도(차이 6.9), 모터전류(차이 2.38) — max가 멀리 튄 열
# 오일온도 max 행: 2020-03-03 12:36:57, 10.19, -0.02, 10.18, 75.0, 3.79, 가동
# 모터전류 max 행: 2020-03-03 06:31:23, 10.05, -0.02, 10.05, 72.0, 6.19, 가동

# 3 모터전류처럼 고른 열과 비교해 차이를 설명
# 압축압력은 75%(9.67)와 max(10.22) 차이 0.56으로 좁음 — 분포가 고름
# 오일온도는 75%(68.1)와 max(75.0) 차이 6.9로 넓음 — 상위 구간에 과열 극단치 존재

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 실습 7. 통계량 문장으로 묘사
# describe 통계를 자기 말로 풀어 설명
#
# - df['오일온도'].describe(): 특정 핵심 센서 열만 집어서 통계량을 집중 추출합니다.
# - 평균값 약 63.2℃ 로 계산되며, 이를 바탕으로 "지하철 공기압축기 오일온도는
#  평소 약 63.2℃ 근처에서 정상 작동한다"라고 기술 리포트 문장으로 풀어냅니다.
# -----------------------------------------------------------------------------

# 설비 센서 데이터의 "한 열(1 column)"을 묘사
df_oil = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")

# 오일온도 컬럼만 떼서 형태 정보 보기
df_oil["오일온도"].info()

# 오일온도 컬럼만 떼서 describe 통계 보기
print(df_oil["오일온도"].describe())
# count    199.000000
# mean      63.181910 (평균)
# std        6.249822 (표준편차)
# min       50.100000 (최소값)
# 25%       58.100000
# 50%       62.900000 (중앙값)
# 75%       68.100000
# max       75.000000 (최대값)
# Name: 오일온도, dtype: float64
