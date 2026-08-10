# reshpae로 형태 바꾸기
# size로 확인되는 값 개수는 같아야 한다!!!

import numpy as np

under_ten = np.arange(10)
print(under_ten)
print(f"ndim: {under_ten.ndim}")  # 1
print(f"shape: {under_ten.shape}")  # (10,)
print(f"size: {under_ten.size}")  #  10

reshape_ten = under_ten.reshape(2, 5)
print(reshape_ten)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
print(f"ndim: {reshape_ten.ndim}")  # 2
print(f"shape: {reshape_ten.shape}")  # (2, 5)
print(f"size: {reshape_ten.size}")  #  10 -> 안바뀜!!!

# flatten으로 1차원 만들기
flatten_ten = reshape_ten.flatten()
print(flatten_ten)  # [0 1 2 3 4 5 6 7 8 9]
