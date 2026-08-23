import pandas as pd

df = pd.read_csv('data/15_01_사출성형_공정.csv', encoding='utf-8', na_values=[-999, 999])

print(df.shape) # (250, 22)

# NaN 결측 데이터가 있는 "행"들을 모두 삭제
clean = df.dropna() 
print(clean.shape) # (76, 22) -> 이정도면 2/3 이상이 날아가벼림 ㅠㅠ

# NaN 결측 데이터가 있는 "열"들을 모두 삭제
clean2 = df.dropna(axis=1)
print(clean2.shape) # (250, 10) -> 절반 이상의 컬럼 삭제

