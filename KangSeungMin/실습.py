# 실습 1. 딕셔너리 만들고 다루기

# 1) 센서명을 key로, 센서값을 value로 하는 딕셔너리 만들기
sensors = {"모터온도": 78, "진동": 0.5}

# 2) 키로 값을 꺼내고 새 키로 추가, 기존 키로 수정
print(sensors["진동"])  # 값 꺼내기
print(sensors.get("진동", 0))  # 값 더 안전하게 꺼내기

sensors["압력"] = 95  # 새 키로 값 추가
sensors["진동"] = 0.3  # 기존 키로 값 수정

print(sensors)

# 3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 여부 확인
print(sensors.get("면적", -1))
print("진동" in sensors)
print("면적" in sensors)

# 실습 2. update로 여러 값 한 번에 갱신

sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 80, "유량": 42}
sensors.update(new_data)

print("갱신된 딕셔너리")
del sensors["유량"]
print("센서 수:", len(sensors))

# 실습 3. 딕셔너리로 통계내기

sensors = {"모터온도": 58, "압력": 95}
avg = sum(sensors.values()) / len(sensors)
print("평균:", avg)

max_name = ""
max_value = 0

for name, value in sensors.items():
    if value > max_value:
        max_value = value
        max_name = name
print("최대값 센서:", max_name, max_value)

# 실습 4. zip으로 센서명-값 매핑하기

names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))
print(sensors)
for name, value in sensors.items():
    print(name, value)

# 실습 5. 임계값으로 경고 센서 분류하기

values = {"온도": 95, "압력": 88}
limits = {"온도": 90, "압력": 90}

warning = []

for name, value in values.items():
    if value > limits[name]:
        warning.append(name)

print("경고 센서:", warning)
