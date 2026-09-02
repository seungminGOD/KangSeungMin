import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")

process_map = {
    "SNT": "소결",
    "CKO": "코크스",
    "BF": "고로",
    "BOF": "전로",
    "CCM": "연주",
    "HSM": "열간압연",
    "CRM": "냉간압연",
    "UTL": "유틸리티",
}

measure_map = {
    "VIB": "진동",
    "CUR": "전류",
    "SPD": "속도",
    "PRS": "압력",
    "TMP": "온도",
    "FLW": "유량",
}

upper = ["소결", "코크스", "고로", "전로", "연주"]

df["공정"] = df["tag"].str.split("-").str[1].map(process_map)

df["상하공정"] = df["공정"].apply(lambda x: "상공정" if x in upper else "하공정")

df["계측항목"] = df["tag"].str.split("-").str[-1].map(measure_map)

print("[24개 태그 판정표]")
print(df[["tag", "공정", "상하공정", "계측항목"]].to_string(index=False))

process_count = df["공정"].value_counts()
top_process = process_count[process_count == process_count.max()].index.tolist()

print("\n[CASE A 공정별 태그 수]")
print(process_count)
print("가장 많은 공정:", ", ".join(top_process), f"({process_count.max()}개)")

measure_count = df["계측항목"].value_counts()
top_measure = measure_count[measure_count == measure_count.max()].index.tolist()

print("\n[CASE B 계측항목별 태그 수]")
print(measure_count)
print("가장 많은 물리량:", ", ".join(top_measure), f"({measure_count.max()}개)")
