def say_hello():
    pass


def say_hi():
    print("안녕")


say_hi()


def show_hello():
    name = "Min"
    print(f"안녕하세요, {name}")


name = "jun"
show_hello("Min")


def show_hi(name, message):
    message = "안녕하세요"
    print(f"{message},{name}")


show_hi("Min")

# 매개변수에는 따로 안 알려주면 기본값을 적용할 수 있음


def show_greeting(name, message="안녕하세요"):
    print(f"{message},{name}")


show_greeting("Min", message="Hello")
