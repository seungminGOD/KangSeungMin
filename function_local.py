# 지금까지 배운 내용을 활용해서
# 재미있는 함수 만들기 예제

import random

groups = ["에스파", "하트2하트", "리센느", "태연", "엔믹스"]

# 랜덤 뽑기!
my_group = random.choice(groups)
print(my_group)


def get_random_group():
    groups = [
        {"이름": "에스파", "리더": "카리나"},
        {"이름": "엔믹스", "리더": "해원"},
        {"이름": "리센느", "리더": "원희"},
    ]

    my_group = random.choice(groups)

    return my_group.get("이름"), my_group.get("리더")


group_name, group_leader = get_random_group()
print(f"{group_name}의 리더는 {group_leader}입니다")
