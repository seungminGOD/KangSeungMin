import numpy as np

# 실습 3. 센서값 정규화하기
# 목표 : 회전수 배열을 0과 1 사이 값으로 정규화

# 회전수 측정 배열 준비
rpm3 = np.array([1551, 1408, 1498, 1433, 1425, 2861])

# 최솟값과 최댓값을 min, max로 확인
print(rpm3.min())  # 1408
print(rpm3.max())  # 2861

# 정규화 공식을 브로드캐스팅으로 적용해 변환
# 정규화 공식
# 정규화된X = (비교대상X - 최소값) / (최대값 - 최소값)
rpm_min = rpm3.min()
rpm_max = rpm3.max()
normalized = (rpm3 - rpm_min) / (rpm_max - rpm_min)
print(normalized)
# [0.09841707 0.         0.06194081 0.01720578 0.01169993 1.        ]
# 소숫점 이하값이 너무 길어진다면 numpy 배열에서 제공하는 round 기능을 활요
print(np.round(normalized, 2))
# [0.1  0.   0.06 0.02 0.01 1.  ]
