# 실습 1. CSV 불러오기 워밍업

import pandas as pd
import os

filepath = os.path.join("data", "12_metro_small.csv")  # "data/12_metro_small.csv"

try:
    df = pd.read_csv(
        filepath,
        encoding="utf-8",
        sep=",",
        index_col="측정시각",
        nrows=5,
        usecols=["측정시각", "가동상태"],
    )
    print(df.shape)  # (30, 7)

    print(df.head(10))
except FileNotFoundError:
    print(f"파일이 없습니다 : {filepath}")
