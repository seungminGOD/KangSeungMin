# list는 python의 자료형 중 하나
# 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

temps = [35, 36, 37, 38]  # int 리스트
float_temps = [36.4, 36.5, 36.6, 36.7]  # float 리스트
machines = ["펌프", "압축기", "모터"]  # string 리스트

# 리스트는 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
print(temps[2])  # 37 > 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# 리스트 안에 몇 개의 값이 담겼는진 모르지만 마지막 요소를 뽑고 싶다면
print(temps[-2])  # 가장 마지막 요소 출력

# 빈 리스트
empty = []

# 리스트에 담긴 값의 갯수 세기
# len() 내장함수 사용
print(len(temps))
print(len(empty))

# 리스트의 담긴 값의 갯수 변수에 저장
temps_length = len(temps)
print(temps_length)  # 4

temps = [20, 25, 23, 27, 26]
print(temps)  # [20, 25, 23, 27, 26]
print(len(temps))  # 5
empty = []
print(len(empty))  # 0

# 리스트의 인덱스
print(temps[0], temps[-1])
# -1을 사용하는 이유는 최신 값은 대체로 뒤에 추가가 됨
# 가장 최근 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이 -1로 계산이 가능하지만 이 작업이 번거로워 -1을 가장 많이 사용

# 없는 인덱스 호출
# temps 리스트는 길이가 5
# print(temps[5])  # IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

temps = [28, 32, 33, 29, 26, 23]
print(temps[0])  # 28
print(temps[2])  # 33
print(temps[-1])  # 23

output = [120, 95, 130, 110, 88, 102]
first = output[0]
last = output[-1]
print(first + last)  # 222
print((first + last) / 2)  # 111.0

# 리스트의 자료형
print("=== 리스트의 자료형 ===")

# temps라는 리스트 자체
print(f"temps: {temps}")
print(f"type(temps): {type(temps)}")

# temps라는 리스트의 0번째 인덱스 요소
print(f"temps[0]: {temps[0]}")
print(f"type(temps[0]): {type(temps[0])}")

print(type(float_temps[0]))
print(type(machines[0]))

# 퀴즈
# mixed = ["펌프", 78, True]

print(type(mixed[1]))
print(type(mixed[-1]))
