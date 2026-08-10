# 1. 현재 경로 가상환경 생성
# python -m venv .venv


# 2. 가상환경 활성화
# source .venv/Scripts/activate
# (pip install numpy)

# 3. 작업 후 가상환경 종료
# deactivate

import numpy as np

numbers = [1, 2, 3, 4, 5]

np_numbers = np.array(numbers)
print(np_numbers)
