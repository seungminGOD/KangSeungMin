# 실습 4 참고

import numpy as np

# 웬만하면 2차원 배열을 만들어주세요
apt_games = np.array([
    [3, 6, 9],
    [4, 8, 10]
])

print(apt_games)
# [[ 3  6  9]
#  [ 4  8 10]]

# ndim 차원확인
print(apt_games.ndim) # 2

# shape 형태확인
print(apt_games.shape) # (2, 3)

# size 전체 개수 확인
print(apt_games.size) # 6
