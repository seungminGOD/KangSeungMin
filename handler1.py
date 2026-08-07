# 트레이스백으로 에러 읽기

# ValueError: 글자를 숫자로 변환 요구 - 당연히 실패
# temp = int("스믈")

# Traceback (most recent call last):
#   File "/Users/nedpark/Desktop/handler1.py", line 4, in <module>
#     tmep = int ("스믈")
#            ~~~~^^^^^^^^
# ValueError: invalid literal for int() with base 10: '스믈'

# 정상화
temp = int("20")
print(temp)

print("=" * 20)

# ZeroDivisionError : 숫자는 0으로 나뉠 수 없어요
# result = 10 / 0

# Traceback (most recent call last):
#   File "/Users/nedpark/Desktop/handler1.py", line 19, in <module>
#     result = 10 / 0
#              ~~~^~~
# ZeroDivisionError: division by zero

# 정상화
result = 10 / 3
print(result)

print("=" * 20)

# NameError : 그런 이름도 있었어요?라는 뜻의 에러
# hello()

# Traceback (most recent call last):
#   File "/Users/nedpark/Desktop/handler1.py", line 32, in <module>
#     hello()
#     ^^^^^
# NameError: name 'hello' is not defined. Did you mean: 'help'?

# 정상화
print("Hello")
