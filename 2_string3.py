print("지금 날씨는 17도 입니다.")

print("지금 날씨는 %d도입니다." % 30)



# 실시간으로 동시에 변경할때 활용한다.
a = 20
print("지금 전국 평균기온은 %d도입니다." % a)
print("지금 서울 날씨는 %d도입니다." % a)
print("지금 울산 날씨는 %d도입니다." % a)
print("지금 아산 날씨는 %d도입니다." % a)
print("지금 대전 날씨는 %d도입니다." % a)
print("지금 부산 날씨는 %d도입니다." % a)



print("지금 날씨는 %s도입니다." % "삼십")

b = "파이썬"
print("오늘 수업은 %s입니다." % b)
print("내일 수업은 %s입니다." % b)
print("모래 수업은 %s입니다." % b)
print("다음주 수업은 %s입니다." % b)

c = 1.23
print("지금 날씨는 %d이고, 수업은 %s이고, %s %s %.2f이 있습니다" % (20, b, b, b, c))

# %d 숫자, %s 문자열, %f 소수점을 자주 사용
# %.숫자f : 소수점 숫자 자리만큼 표시된다.

# %d, %s, %.2f를 사용해서 사과를 "3"개 먹었고, 수업언어는 "파이썬"이고, 날씨는 "17.56"도 입니다.
a = 3
b = "파이썬"
c = 17.56
print("사과를 %d개 먹었고, 수업 언어는 %s이고, 날씨는 %.2f도 입니다." %(a, b, c))


# 문장 끝나고 .format(숫자 or "문자")입력하여 바꿔준다.
print("사과를 {0}개 먹었다.".format(3))
print("사과를 {0}개 먹었다.".format("한"))

print("사과를 {0}개 먹고, 배를 {1}개 먹었다.".format(1, '세'))

d = 3
e = "두"
print("사과를 {0}개 먹고, 배를 {1}개 먹었다.".format(d, e))


print("사과를 {number}개 먹고, 배를 {number2}개 먹었다.".format(number = 1, number2 = 9))


# 아침 "9"시에 수업을 "시작"했고, 드디어 "마칠시간"입니다. "축하"합니다.
# 1. time 2. start 3. end 4. cong
a = 9
b = "시작"
c = "마칠시간"
d = "축하"
print("아침 {time}시에 수업을 {start}했고, 드디어{end}입니다. {cong}합니다.".format(time = a, start = b, end = c, cong = d))