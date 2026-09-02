import pandas as pd
# 02-01_측정의_3요소_설비태그목록
# 02-01_측정의_3요소_측정샘플

tags = pd.read_csv("02-01_측정의_3요소_설비태그목록.csv")
df = pd.read_csv("02-01_측정의_3요소_측정샘플.csv")

##### 실습1

#   - 케이스 A : 회전기계 계통 (MTR 로 시작하는 태그)
#   - 케이스 B : 유압·열설비 계통 (HYD, FUR 로 시작하는 태그)

# tag,description,unit,sampling_sec,range_min
# range_max,resolution,install_location

##### case A
print(tags["tag"].str.startswith("MTR")) # tag컬럼에서 MTR로 시작되는지 검사: T/F 

# 대괄호 안에 조건식 -> True인 데이터만 모아서 저장
case_a= tags[tags["tag"].str.startswith("MTR")] 
# print(case_a)

##### case B
print(tags["tag"].str.startswith(("HYD", "FUR")))
case_b = tags[tags["tag"].str.startswith(("HYD", "FUR"))] 
print(case_b)

##### 실습2
df["timestamp"] = pd.to_datetime(df["timestamp"])
gaps = df["timestamp"].diff().value_counts()
print(gaps)
# 0 days 00:01:00    119
# Name: count, dtype: int64

##### 실습3, 최솟값, 최댓값, 평균, 값이 변하는 최소 폭
cols =["MTR01_VIB_RMS_H","MTR01_CURRENT","MTR01_TEMP",
       "HYD01_PRESS_IN","FUR01_TEMP_Z1"]

print(df[cols].agg(["min", "max", "mean"]).round(2))

# 값이 변하는 최소 폭
for c in cols:
    changes = df[c].diff().abs() # 절댓값의 차이를 모아둔 데이터프레임

    # changes 데이터 프레임에서 0을 제외하고 최솟값을 가지고 오고 있는 중.
    min_change = changes[changes>0].min() 
    repeated = (changes==0).sum()
    print("태그 이름, 최소 차이, 반복횟수", c,round(min_change, 2), repeated)