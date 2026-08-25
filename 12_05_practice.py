# 실습 3. 한글·구분자 깨짐 옵션 다루기
# encoding과 sep으로 깨진 파일을 직접 해결

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면 200행 7열

import pandas as pd

df = pd.read_csv("data/12_metro_compressor_semicolon.csv", sep=";", encoding="utf-8")
print(df.shape)  # (200, 1)
print(df.head(4))
