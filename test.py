import pandas as pd

CD = "data/16_diecasting.csv"

df = pd.read_csv(CD)


# ===== 실습 1 =====
Q1 = df["사이클타임"].quantile(0.25)
Q3 = df["사이클타임"].quantile(0.75)

IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("실습 1")
print(round(Q1, 2), round(Q3, 2), round(IQR, 2))
print(round(lower, 2), round(upper, 2))


# ===== 실습 2 =====
mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)

print("\n실습 2")
print(df[mask][["샷", "사이클타임", "상태"]])
print(mask.sum(), round(mask.mean() * 100, 1))


# ===== 실습 3 =====
print("\n실습 3")
print("matplotlib 실습이라 생략")


# ===== 실습 4 =====
정상 = df[~mask]

print("\n실습 4")
print(len(df), len(정상))
print(round(df["사이클타임"].mean(), 2))
print(round(정상["사이클타임"].mean(), 2))


# ===== 실습 5 =====
보정 = df["사이클타임"].clip(lower=lower, upper=upper)

print("\n실습 5")
print(round(보정.min(), 2), round(보정.max(), 2))
print(round(보정.mean(), 2))


# ===== 실습 6 =====
Q1 = df["실린더압력"].quantile(0.25)
Q3 = df["실린더압력"].quantile(0.75)

IQR = Q3 - Q1
L = Q1 - 1.5 * IQR
U = Q3 + 1.5 * IQR

m = (df["실린더압력"] < L) | (df["실린더압력"] > U)

채움 = df["실린더압력"].mask(m)
채움 = 채움.fillna(채움.median())

print("\n실습 6")
print(round(df["실린더압력"].mean(), 2))
print(round(df[~m]["실린더압력"].mean(), 2))
print(round(df["실린더압력"].clip(L, U).mean(), 2))
print(round(채움.mean(), 2))


# ===== 실습 7 =====
print("\n실습 7")
print(df.duplicated().sum())
print(df[df.duplicated()])
print(df.duplicated(keep=False).sum())