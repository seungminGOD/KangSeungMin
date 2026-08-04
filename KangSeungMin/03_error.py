# print(NameError 만들기)  # SyntaxError 발생 (띄어쓰기가 있어서 변수 2개를 쉼표 없이 작성했다고 추정)
# print(NameError만들기)  # NameError 발생
# 코드는 위에서 아래로 실행되기 때문에 위에서 에러 발생하면 그 이후 코드 실행 X
print("NameError 만들기")  # 따옴표로 감싸주면 에러 발생 X

# ===============================
print("======SyntaxError 만들기======")

# print("온도) # 따옴표를 안닫음
# print("진동" # 괄호를 안닫음

print("온도")
print("진동")
