# Study.py — 4단계: if / else (조건문)

# =============================================================================
# [개념]
# - 조건이 참이면 if 블록 실행, 아니면 else 실행
# - 들여쓰기(탭/스pace 4칸) 필수!
# =============================================================================

# score = 75
# if score >= 60:
#     print("합격")
# else:
#     print("불합격")


# =============================================================================
# [연습] — 필요할 때만 주석 풀기 (2개만)
# =============================================================================

# 연습 1.
# age = 20
# if age >= 19:
#     print("성인")
# else:
#     print("미성년")

# 연습 2.
# temp = 85
# if temp > 80:
#     print("과열")
# else:
#     print("정상")


# =============================================================================
# [응용 10문제]  ★ 1~7 보통  /  8~10 매우 어려움
# =============================================================================

# ── 보통 ──────────────────────────────────────────────────

# 1. rpm=4500 → 4000 초과면 "과다", 아니면 "정상" 출력
# (여기에 작성)
rpm = 4500
if rpm > 4000:
    print("과다")
else:
    print("정상")

# 2. oil=55 → 60 미만이면 "저온", 아니면 "정상" 출력
# (여기에 작성)
oil = 55
if oil < 60:
    print("저온")
else:
    print("정상")


# 3. quality="불량" → 불량이면 "재작업", 아니면 "출하" 출력
#    (글자 비교는 == 사용, 예: quality == "불량")
# (여기에 작성)

quality = "불량"
if quality == "불량":
    print("재작업")
else:
    print("출하")

# 4. motor=0.03 → 0.05 미만이면 "정지", 아니면 "가동" 출력
# (여기에 작성)
motor = 0.03
if motor < 0.05:
    print("정지")
else:
    print("가동")

# 5. cycle=650 → 100 초과면 "이상", 아니면 "정상" 출력
# (여기에 작성)
cycle = 650
if cycle > 100:
    print("이상")

# 6. force=250 → 240 이상이면 "양호", 아니면 "부족" 출력
# (여기에 작성)


# 7. count=0 → count가 0이면 "데이터 없음", 아니면 "데이터 있음"
#    힌트: 같음은 ==
# (여기에 작성)

count = 0
if count == 0:
    print("데이터 없음")
else:
    print("데이터 있음")


# ── 매우 어려움 ──────────────────────────────────────────

# 8. score=87 → elif로 등급 출력
#    90 이상 "A" / 80 이상 "B" / 70 이상 "C" / 나머지 "D"
#    힌트: if → elif → elif → else 순서
# (여기에 작성)

score = 87
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")

else:
    print("D")

# 9. rpm=4200, torque=8 → 두 조건 모두 만족할 때만 "위험" 출력
#    조건: rpm > 4000 이고 torque < 15
#    힌트: and 사용  →  if rpm > 4000 and torque < 15:
#    하나라도 아니면 "안전" 출력
# (여기에 작성)
rpm = 4200
torque = 8
if rpm > 4000 and torque < 15:
    print("위험")
else:
    print("안전")


# 10. cylinder=108, cast=522 → 불량 판정 프로그램
#     ① defect = cast / cylinder  (실린더 대비 주조압력 비율)
#     ② defect가 6.0 이상이면 "비율 이상"
#        아니면 "비율 정상" 출력
#     ③ 그 다음 줄에서 cylinder가 150 미만이면 "압력 부족" 추가 출력
#        (if를 2번 써도 됨)
# (여기에 작성)

cylinder = 108
cast = 522
defect = cast / cylinder

if defect >= 6.0:
    print("비율 이상")
elif cylinder < 150:
    print("압력 부족")
else:
    print("비율 정상")

# =============================================================================
# [정답] — 다 해본 뒤에만 확인!
# =============================================================================
# 1. rpm=4500  /  if rpm>4000: print("과다") else: print("정상")
# 2. oil=55  /  if oil<60: print("저온") else: print("정상")
# 3. quality="불량"  /  if quality=="불량": print("재작업") else: print("출하")
# 4. motor=0.03  /  if motor<0.05: print("정지") else: print("가동")
# 5. cycle=650  /  if cycle>100: print("이상") else: print("정상")
# 6. force=250  /  if force>=240: print("양호") else: print("부족")
# 7. count=0  /  if count==0: print("데이터 없음") else: print("데이터 있음")
#
# 8. score=87
#    if score>=90: print("A")
#    elif score>=80: print("B")
#    elif score>=70: print("C")
#    else: print("D")
#
# 9. rpm=4200  /  torque=8
#    if rpm>4000 and torque<15: print("위험")
#    else: print("안전")
#
# 10. cylinder=108  /  cast=522
#     defect = cast / cylinder
#     if defect >= 6.0: print("비율 이상")
#     else: print("비율 정상")
#     if cylinder < 150: print("압력 부족")
