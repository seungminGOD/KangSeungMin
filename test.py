# 실습 1. 센서값 배열 만들기

import numpy as np

miles = np.array([94.7, 89.3, 90.5, 88.7, 92.1])

print(miles * 1.60934)

import numpy as np


# 실습 2.

gab_six = np.arange(0, 50, 10)
print(gab_six)

div_six = np.linspace(0, 40, 8)
print(div_six)

# 실습 3.

import numpy as np

check_point = np.arange(0, 100, 10)
print(check_point)


# 실습 4.

import numpy as np

apt_games = np.array([[3, 6, 9], [4, 8, 10]])

print(apt_games)
# [[ 3  6  9]
#  [ 4  8 10]]

print(apt_games.ndim)

print(apt_games.shape)

print(apt_games.size)


# 실습 5. 자료형 확인과 변환하기

import numpy as np

data = np.array([5343.232, 2950.332, 119.44])

print(data.dtype)

converted_data = data.astype(int)
print(converted_data)


# 실습 6. 배열 모양 바꾸기

import numpy as np

numbers = np.arange(6)
print(numbers)

converted_numbers = numbers.reshape(2, 3)

print(converted_numbers)


# 실습 7. 센서 데이터 표로 정리하기
import numpy as np

data = np.arange(10)

converted_data = data.reshape(2, 5)

print(converted_data)


# 실습 8. 배열 생성부터 정리까지

import numpy as np

data = np.array([2.3, 7.9, 1.1, 5.8, 5.4, 7.6])

# shape과 dtype으로 구조 확인
print(f"shape: {data.shape}")
print(f"dtype: {data.dtype}")

converted = data.reshape(3, 2)
print(converted)
