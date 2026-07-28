s = "WARNING"
small = s.lower()
print(small)  # warning

print("=== .strip() ===")

# 공백 제거
# .strip(): 앞과 뒤 모든 공백 제거
# .lstrip(): 왼쪽 공백 제거
# .rstrip(): 오른쪽 공백 제거

raw = "   정상    "
print(raw.strip())  # "정상"
print(raw.lstrip())  # "정상    "
print(raw.rstrip())  # "   정상"

# 문자열의 가운데 공백은 strip으로 지우지 못함
print("    정    상    ".strip())  # "정    상"

print(raw)  # "   정상    "
# strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발


# strip으로 문자 제거
str4 = "===정상==="
print(str4.strip("="))
# 인자로 전달한 양 끝의 =이 제거됨

str5 = "=정상========"
print(str5.strip("="))  # "정상"
# 갯수 상관 없이 인자로 전달한 문자를 양 끝에서 제거
print(str5.strip("= "))  # "정상"

str6 = "==정==상===="
print(str6.strip("="))  # "정==상"


print("=== 체이닝 ===")

raw = "   NORMAL    "
step1 = raw.strip()  # "NORMAL"
step2 = step1.lower()  # "normal"

chain = raw.strip().lower()

raw = raw.strip().lower()

str7 = "      Warning  "

str7 = str7.strip()
print("[" + str7 + "]")

str7 = str7.strip().lower()
print("[" + str7 + "]")

str8 = "aaab 이렇게? cd"
print(str8.strip("abcd"))
print(str8.strip("abcd "))

print("=== replace() ===")

print("정 상 가 동".replace(" ", ""))

num = 1
num = num + 1  # 2
num += 1  # 3

# ===========================================
print("=== f-string ===")

name = "PUMP_A"
temp = 36

# 출력 결과: 설비 PUMP_A, 온도 36도
print("설비 " + name + ", 온도 " + str(temp) + "도")

# f-string
print(f"설비 {name}, 온도 {temp}도")
# 따옴표 밖에 f 작성하기
# 변수명은 꼭 중괄호에 감싸기

# f-string 연산
hour = 8

# 우리는 하루에 8시간 수업을 듣고, 이는 480분입니다.
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분입니다.")
# ======================================
kor = 90
eng = 85
math = 86

print(f"평균 {(kor + eng + math) / 3}")

# ======================================
value = 25.34567
print(f"측정값 {value}")
print(f"측정값 {value:.2f}")
print(f"측정값 {value:.1f}")

num = 87.456
print(f"{num:.1f}")
print(f"{num:.2f}")

# ======================================
raw = " 5, sensor_2, WARNING, 0.78912 "
parts = raw.strip().split(",")
sid = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())
print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")
