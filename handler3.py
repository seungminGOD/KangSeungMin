# 08-06 실습 2

origin = input("온도 :")
print(f"입력한 온도는 {origin}")

try:
    temp = int(origin)
except ValueError:
    print("숫자 아니면 왜 저를 부르셨어요?")
    temp = 0

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")
