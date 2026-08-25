import pandas as pd

df = pd.read_csv('data/16_diecasting.csv', encoding='utf-8')

# 실습 3. 정렬해서 이상치 후보 찾기
# 정렬로 동떨어진 사이클타임을 눈으로 찾아 분류

# 단계
# · 사이클타임 열을 기준으로 내림차순 정렬
s_sorted = df.sort_values('사이클타임', ascending = False)


# · 위쪽 끝에서 동떨어진 큰 값 찾기
print(s_sorted.head()) # 6170.0, 652.3  발견!

# · 각 후보를 정상 상태와 이상 상태로 나누기
# 맨 위 6170초 = 설비 잼(상태 1). 100초 넘는 샷도 이상 후보. 정상 사이클은 20~35초 부근.

# 예상 결과
# 6170·652초 등 설비 잼 후보, 정상은 20~35초