import pandas as pd
df = pd.read_csv('data/14_hydraulic.csv', encoding = 'utf-8')

# corr 한 줄로 계산하는 상관계수 : correlation
cor1 = df['온도'].corr(df['진동'])
print(cor1) # 0.9307966383117151 
print(cor1.round(3)) # 0.931
print(round(cor1, 3)) # 0.931
print(round(df['온도'].corr(df['진동']), 3)) # 0.931
print(df['온도'].corr(df['진동']).round(3)) # 0.931 높은 상관관계

print(df['온도'].corr(df['압력']).round(3)) # 0.284 낮은 상관관계
print(df['진동'].corr(df['압력']).round(3)) # 0.524 중간쯤 상관관계

# 세가지를 동시에 비교하자
num = df[['온도', '진동', '압력']]
print(num.corr().round(3))
#        온도     진동     압력
# 온도  1.000  0.931  0.284
# 진동  0.931  1.000  0.524
# 압력  0.284  0.524  1.000