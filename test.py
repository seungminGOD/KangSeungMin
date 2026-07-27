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
# ======================================================================


print("=== split() ===")
# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

drinks = "에스프레소 아메리카노 카페라떼"
print(drinks.split())  # 인자를 보내지 않음

fruits = "딸기,거봉,키위,사쿠란보"
print(fruits.split(","))

# split 횟수 제한
num = "010-1234-5678"

print(num.split("-", 1))
