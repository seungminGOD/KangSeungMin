# 실습 1. CSV 불러오기 워밍업

import pandas as pd
import os

filepath = os.path.join("data", "12_metro_small.csv")

try:
    df = pd.read_csv(
        filepath,
        encoding="utf-8",
        usecols=["측정시각", "압축압력", "오일온도", "모터전류"],
        parse_dates=["측정시각"],
        nrows=8,
    )
    print(df.shape)  # (8, 4)
    print(df.head())
    print(df.dtypes)
except FileNotFoundError:
    print(f"파일이 없습니다 : {filepath}")


# 실습 2. 설비 센서 CSV 불러오기
import pandas as pd
import os

# 12_metro_compressor.csv
# 200행 7열 — 인덱스 3번 행 오일온도가 NaN

filepath = os.path.join("data", "12_metro_compressor.csv")
df_sensor = pd.read_csv(filepath, encoding="utf-8", parse_dates=["측정시각"])

print(df_sensor.columns.tolist())
print(df_sensor.head(5))
print(df_sensor.iloc[3])  # 오일온도 NaN 행 확인
print(df_sensor.shape)  # (200, 7)
print(df_sensor.isna().sum())


# 실습 3. 한글·구분자 깨짐 옵션 다루기
# encoding과 sep으로 깨진 파일을 직접 해결

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면 200행 7열

import pandas as pd
import os

filepath = os.path.join("data", "12_metro_compressor_semicolon.csv")

df_wrong = pd.read_csv(filepath, encoding="utf-8")
print(df_wrong.shape)  # (200, 1)

df = pd.read_csv(filepath, sep=";", encoding="utf-8")
print(df.shape)  # (200, 7)
print(df.columns.tolist())
print(df.head(3))


# 실습 4. 필요한 열만 골라 불러오기
# G O A L usecols와 nrows로 열 많은 데이터에서 필요한 부분만

# 압력 센서 3개 + 측정시각만 골라 불러오기
# usecols + nrows → 15행 4열

import pandas as pd
import os

filepath = os.path.join("data", "12_metro_compressor.csv")
df = pd.read_csv(
    filepath,
    encoding="utf-8",
    usecols=["측정시각", "압축압력", "배출압력", "저장압력"],
    parse_dates=["측정시각"],
    nrows=15,
)
print(df.shape)  # (200, 7) -> (15, 4)
print(df.columns.tolist())
print(df.head(3))
print(df.tail(2))


# 실습 5. 경로·옵션 오류 고치기
# 오류 메시지를 읽고 스스로 원인을 찾아 고치기

# data/ 누락, 철자, .csv 누락— 세 종류의 FileNotFoundError

import pandas as pd

df = pd.read_csv("너무어렵다.csv")  # FileNotFoundError
print(df.shape)


# 실습 6. read_csv 옵션 종합 연습
# G O A L 경로· 인코딩· 구분자· 열 선택을 한 번에 적용

# 세미콜론+한글 파일에서 필요한 열만
# sep + encoding + usecols → 200행 3열

# 여러 옵션을 함께 써서 shape 확인

# -------------------------------------
# 파일 : data 폴더 안의 12_metro_compressor_semicolon.csv
# sep를 잘 사용해서 여러 컬럼이 읽히도록 해주세요
# encoding도 지정해주세요
# 모든 컬럼을 다 읽지는 마시고, '측정시각', '오일온도', '모터전류' 컬럼만 읽어주세요

import pandas as pd
import os

filepath = os.path.join("data", "12_metro_compressor_semicolon.csv")
df = pd.read_csv(
    filepath,
    sep=";",
    encoding="utf-8",
    usecols=["측정시각", "오일온도", "모터전류"],
    parse_dates=["측정시각"],
)

print(df.shape)  # (200, 3)
print(df.dtypes)
print(df.head(3))
print(df.isna().sum())  # 오일온도 NaN 1개
