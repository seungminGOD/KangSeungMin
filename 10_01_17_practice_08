# 실습 8. 배열 생성부터 정리까지

import numpy as np

# [최종결과]
# 형태와 자료형 확인 후 3행 2열 표로 정리된 배열 출력
# 최종형태 shape : (3, 2)
# 최종형태 size : 3 * 2 = 6

# 센서 측정값을 np.array로 배열 생성
data = np.array([4.5, 3.2, 1.7, 9.8, 5.4, 7.6])

# shape과 dtype으로 구조 확인
print(f"shape: {data.shape}") # (6,)
print(f"dtype: {data.dtype}") # float64

# reshape으로 분석용 표 형태로 정리한 뒤 출력
converted = data.reshape(3, 2)
print(converted)
# [[4.5 3.2]
#  [1.7 9.8]
#  [5.4 7.6]]