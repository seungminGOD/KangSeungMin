tag = "PL1-SNT-FAN-01-VIB"

parts = tag.split("-")
print(parts)

plant = parts[0]  # 공장
process = parts[1]  # 공정
equip = parts[2]  # 설비
unit_no = parts[3]  # 일련번호
measure = parts[4]  # 측정항목

print(plant, process, equip, unit_no, measure)

PROCESS_KR = {
    "SNT": "소결",
    "CKO": "코크스",
    "BF": "고로",
    "BOF": "전로",
    "CCM": "연주",
    "HSM": "열간압연",
    "CRM": "냉간압연",
    "UTL": "유틸리티",
}

# 전로를 출력하려면? (BOF 키)
print(PROCESS_KR["BOF"])

# 없는 태그를 가져오는 것 방지
print(PROCESS_KR.get("BOF1", "미등록"))

MEASURE_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRE": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}

print(MEASURE_KR.get("PRS"))

import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")
print(df.shape)
print(df.columns.tolist())
