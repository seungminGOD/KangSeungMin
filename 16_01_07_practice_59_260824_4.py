import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 실습 6. describe로 격차 큰 컬럼 찾기
# describe 표에서 평균-중앙값 격차 큰 이상치 의심 컬럼 찾기
# describe 표에서 이상치 의심 컬럼을 찾아 해석

# · 여러 공정 컬럼을 describe로 요약
print(df.describe())

# · 요약을 컬럼별로 정리하고 평균과 중앙값 격차 계산
# .T -> describe 결과의 axis를 바꿈
report = (
    df[["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]].describe().T
)
print(report)

# · 격차가 큰 순으로 정렬해 이상치 의심 컬럼 확인
# -> 격차라는 새로운 컬럼을 추가해서 계산결과들을 담기 : 새로운 컬럼이름을 언급하면 추가가 된다
# -> 그 다음에 격차 결과순서로 정렬
report["격차"] = (report["mean"] - report["50%"]).abs()

print(
    report.sort_values("격차", ascending=False)[["mean", "50%", "max", "격차"]].head(3)
)

# 예상 결과
# 주조압력·형체력·사이클타임 등 격차 큰 컬럼 확인
#              mean     50%     max          격차
# 주조압력   848.696809  1037.0  1159.0  188.303191
# 형체력    303.106383   258.0   384.0   45.106383
# 사이클타임   64.750000    22.6  6170.0   42.150000
