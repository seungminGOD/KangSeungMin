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
print(type(mixed))

# 리스트 슬라이싱
# 리스트명[시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략 가능 (문자열과 동일)

# temps = [35, 36, 37, 38]
print(temps[1:3])  # [36, 37]
print(temps[1:2])  # [36]
print(temps[:2])  # [35, 36]
print(temps[:2], temps[3:])  # [35, 36] [38]
print(temps[::1])  # [35, 36, 37, 38]
print(temps[::3])  # [35, 38]
print(temps[100:999])

# 인덱싱 vs 슬라이싱
# 인덱싱 temps[0]은 값 하나(35)
# 슬라이싱 temps[0:2]은 리스트 ([35, 36])
# 슬라이싱은 영역을 잘라내는 역할이기 때문에 리스트를 반환하는 것
# temps[100:999] 에러 발생하지 않음
# 슬라이싱은 '있는 만큼만' 잘라주기 때문에 에러 발생하지 않음

temps = [42, 44, 47, 49, 46, 43, 45, 48, 40, 41]
print(temps[:3])  # [42, 44, 47]
print(temps[-3:])  # [48, 40, 41]
print(len(temps[:3]))  # 3


hours = [12, 15, 18, 20, 17, 14, 22, 25, 28, 24, 19, 16]
first = hours[:6]
second = hours[6:]
print(first)  # [12, 15, 18, 20, 17, 14]
print(second)  # [22, 25, 28, 24, 19, 16]
print(len(first), len(second))  # 6 6

print("원본:", temps)
temps[2] = 999
print("2번 인덱스 값 변경 결과:", temps)

# in (존재 확인)
# machines = ["펌프", "압축기", "모터"]
print("펌프" in machines)
print("펌프" not in machines)

print("프레스" in machines)

# 특정 값의 인덱스 찾기
# machines = ["펌프", "압축기", "모터"]

i = machines.index("압축기")
print(i)

# .index() 메서드는 리스트에서 가장 처음 등장하는 인덱스만 반환
machines2 = ["펌프", "압축기", "모터", "압축기"]

i2 = machines.index("압축기")
print(i2)

temps = [31, 34, 39, 37, 35]
print(39 in temps)  # True

i = temps.index(39)
temps[i] = 33

print(temps)  # [31, 34, 33, 37, 35]
print(39 in temps)  # False

# 리스트 값 추가
# .append(추가할값)
# 리스트의 가장 마지막에 값을 추가
nums = [1, 2, 3, 4, 5]

nums.append(999)
print(nums)

# 만약 원본 리스트와 특정 값을 추가한 리스트 둘 다 필요하다면 원본 리스트를 복사해서 리스트 수정 진행
# nums = [1, 2, 3, 4, 5, 999] > 기존 리스트는 원본으로 둠
new_nums = nums
print(new_nums)

new_nums.append(111)
print("원본 nums 리스트:", nums)
print("복사본 new_nums에 111 append 결과:", new_nums)
# 기대 결과: [1, 2, 3, 4, 5, 999]
# 실제 결과: [1, 2, 3, 4, 5, 999, 111]
# 복사한 메모리 주소에 append를 했기 때문에 원본까지 영향을 받음

# 이를 해결하기 위해서 .copy()라는 메서드를 사용
# new_nums2는 새로운 메모리에 nums 배열을 새로 저장
new_nums2 = nums.copy()
new_nums2.append(222)  # nums 배열에 영향을 미치지 않고 사용
print("원본 nums 리스트:", nums)
print("복사본 new_nums2에 222 append 결과:", new_nums2)

# .insert(위치, 값)
# 리스트에서 원하는 위치에 값을 삽입
# 원본 배열에 바로 삽입
nums.insert(3, 333)
print(nums)

data = [1, 2, 3]
new_data = [7, 8, 9]


# 함수의 반환 개념을안 뒤에 확인할 내용
print(data.extend(new_data))

print(data)


# 정리
# 오늘 꼭 알아야 하는 리스트 수정 메서드와 개념
# .append(): 리스트의 가장 마지막에 값을 추가
# insert(): 첫 번째 인자인 위치 인덱스에 값을 삽입
# extend(): 두 리스트를 하나의 리스트로 합체

temps = []
temps.append(30)
print(temps)
temps.insert(0, 28)
print(temps)  # [28, 30]
temps.extend([31, 32])
print(temps)  # [28, 30, 31, 32]

# 리스트에서 요소 삭제
list1 = ["딸기", "사과", "배", "포도", "수박", "망고"]
list1.remove("수박")
print(list1)

# .pop(인덱스): 인덱스로 특정 요소를 삭제할 때 사용
# 삭제한 인덱스의 값을 반환
list1.pop(0)
print(list1)
print(list1.pop(2))
print(list1)

# del: 인덱스로 리스트의 요소 삭제
# 삭제한 인덱스 값 반환
list1.pop(0)
print(list1)


temps = [25, 26, 24, 28, 26, 999]
temps.remove(999)
print(temps)  # [25, 26, 24, 28, 26]
x = temps.pop(1)
print(x)  # [26]
del temps[0]
print(temps)  # [24, 28, 26]

n = [37, 2, 8, 109, 1004, -1, 22]
print("n 리스트 원본:", n)

n.sort()

# 리스트 안의 값 갯수 구하기
# .count(찾을 값)

f = ["텀블러", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
print(f.count("일회용컵"))
print(f)  # 원본 배열에 변화 없음

# 특정 값의 위치 찾기
# .index(위치를 찾을 값)
print(f.index("일회용컵"))
print(f)
