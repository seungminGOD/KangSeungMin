# 리스트로 크루원들의 이름을 나열
data_class = ["태구", "수진", "영준"]

# 딕셔너리로 정확하게 역할 부여
data_class_dict = {"반장": "태구", "부반장": "수진", "당번": "영준"}

# 센서로부터 얻는 예시 데이터

sensors = {"센서이름": "보일러", "모터온도": 78, "진동": 0.5}

print(sensors)
print(type(sensors))  # 딕셔너리 타입 확인
empty = {}
print(type(empty))

print(sensors["센서이름"])
print(sensors["진동"])
print(sensors["모터온도"])

# 기존에 있던 key 값 변경
sensors["센서이름"] = "펌프"
sensors["진동"] = 0.7

# 기존에 없던 key 값 추가
sensors["펌프압력"] = 95
sensors["유량"] = 42

# 더 이상 필요없는 key와 그 value 삭제
del sensors["펌프압력"]
print(sensors)

print(sensors.get("센서이름"))
print(sensors.get("모터온도"))

motor_degree = sensors.get("모터온도", 0)

next_degree = motor_degree + 10
print(next_degree)

is_motor_degree_key = "모터온도" in sensors
print(is_motor_degree_key)

if is_motor_degree_key:
    print("그런 거 있어요")
else:
    print("그런 거 없어요")

# keys 가져오기
print(sensors.keys())
print(len(sensors.values()))
print(len(sensors))

if len(sensors) < 5:
    print("센서 데이터가 부족합니다.")


for key, value in sensors.items():
    print(key)
    print(value)

for name, value in sensors.items():
    print(name)
    print(value)

# 재미난 사례 추가
# 나라 이름으로 정리
# 유럽: 스페인(ESP), 프랑스(FRA), 독일(DEU), 스위스(SUI), 네덜란드(NLD)
# 아시아: 한국(KOR), 일본(JPN), 중국(CHN), 사우디(SAU), 이란(IRN)
# 남아메리카: 브라질(BRA), 아르헨티나(ARG), 칠레(CHI), 콜롬비아(COL), 우르과이(URU)
# 각 나라마다 이름과 약칭으로 정의 가능

korea = {"국가명": "대한민국", "약칭": "KOR"}
japan = {"국가명": "일본", "약칭": "JPN"}

asia = [korea, japan]
print(asia)

europe = [
    {"국가명": "스페인", "약칭": "ESP"},
    {"국가명": "프랑스", "약칭": "FRA"},
    {"국가명": "독일", "약칭": "DEU"},
    {"국가명": "스위스", "약칭": "SUI"},
    {"국가명": "네덜란드", "약칭": "NLD"},
]
print(europe)

# 포켓몬 1,2,3 진화단계를 딕셔너리로 만들고
# 그 딕셔너리들이 모인 배열 만들기
# 그 배열 데이터를 화면에 print
# 가능하면 그 배열의 데이터들을 for~in을 사용해서 하나씩 꺼내 print (선택사항)

# 리자몽 꼬북이 구구 꼬렛 피죤 이상해씨 케터피 고오스 물짱이 미뇽

pokemon_list = [
    {"1단계": "파이리", "2단계": "리자드", "3단계": "리자몽"},
    {"1단계": "꼬부기", "2단계": "어니부기", "3단계": "거북왕"},
    {"1단계": "구구", "2단계": "피죤 ", "3단계": "피죤투"},
    {"1단계": "꼬렛", "2단계": "레트라", "3단계": "레트라"},
    {"1단계": "피죤", "2단계": "피죤투", "3단계": "피죤투"},
    {"1단계": "이상해씨", "2단계": "이상해풀", "3단계": "이상해꽃"},
    {"1단계": "캐터피", "2단계": "단데기", "3단계": "버터플"},
    {"1단계": "고오스", "2단계": "고우스트", "3단계": "팬텀"},
    {"1단계": "물짱이", "2단계": "슈륙챔", "3단계": "강챙이"},
    {"1단계": "미뇽", "2단계": "비브라바", "3단계": "플라이곤"},
]

# 배열 전체 출력
print(pokemon_list)

print()

# for~in으로 하나씩 출력
for pokemon in pokemon_list:
    print("1단계 :", pokemon["1단계"])
    print("2단계 :", pokemon["2단계"])
    print("3단계 :", pokemon["3단계"])
    print("--------------------")

# 두 딕셔너리를 key-value 조합으로 하나씩 꺼내어 비교하기
# 다음의 두 딕셔너리는 같은 key들을 가지고 있음
# 실제 데이터
values = {"모터온도": 95, "압력": 88}
# 임계치 데이터
limits = {"모터온도": 90, "압력": 90}

for name, value in values.items():
    print(f"{name} : {value}")

    if value > limits.get(name, 0):
        print(name, "경고")

# ==================================================
sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 80, "유량": 42}
sensors.update(new_data)
print(sensors)  # 결과: {'모터온도': 80, '진동': 0.5, '유량': 42}

# zip으로 key들의 배열과 value들의 배열을 묶어서 딕셔너리 만들기
names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(
    zip(names, values)
)  # zip 기능으로 두 배열을 사용해 묶고 dict 타입 딕셔너리로 만들기
print(sensors)  # 결과: {'모터온도': 78, '진동': 0.5, '압력': 95}

# 딕셔너리 안에 value로 딕셔너리를 사용
kbo = [
    {
        "구단명": "삼성",
        "마스코트": "라이온스",
        "구장": {"1구장": "대구라이온스파크", "2구장": "포항야구장"},
    },
    {
        "구단명": "두산",
        "마스코트": "베어스",
        "구장": {"1구장": "잠실야구장", "2구장": "베어스파크"},
    },
]

# 쉽게 배열 안에 딕셔너리 안에 딕셔너리 접근
print(kbo[0]["구장"])

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

print("test")
