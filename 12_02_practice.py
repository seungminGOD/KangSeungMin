# 실습 1. CSV 불러오기 워밍업

import pandas as pd
import os


filepath = os.path.join("data", "12_metro_small_2.csv")

try:
    df = pd.read_csv(filepath)
    print(df.shape)  # (30, 7)

    print(df.head(2))
except FileNotFoundError:
    print(f"파일이 없습니다 : {filepath}")
