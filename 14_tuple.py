# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 python이 튜플로 인식
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = ()  # 괄호 있고, 쉼표 없고, 값도 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 요소 갯수
# 요소 2개 이상: 쉼표가 있다면 튜플
# 요소 1개: 쉼표 여부
# 요소 0개: ()번 괄호

# 튜플에서 많이 헷갈려하는 부분
# (1): int
# (2): tuple

# (1,2,3,) 가장 마지막에 쉼표를 붙여 튜플임을
# (1,2,3) 튜플 맞음

sensor = (
    "모터온도",
    78,
)

# 튜플의 인덱스
print(sensor[0])

# 튜플의 슬라이싱
s = (
    "a",
    "b",
    "c",
    "d",
    "e",
)
print(s[1:4])
print(type(s[1:4]))

a, b, c = "a", "b", "c"
print(a)
print(b)
print(c)

# unpacking = (
# 1. # 변수 1
# 2. # 변수 2
# 3. # 변수 3
# )

one, two, three = unpacking
print("one:", one)
print("two:", two)
print("three:", three)
