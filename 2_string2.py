# 문자열 연산하기

head = "Python"
tail = " is fun!"
total = head + tail

print(head + tail)
print(total)

print(total * 2)



# 문자열 곱하기를 응용하기

print('-' * 50)
print("문자열 곱하기 표시")
print('-' * 50)

print()
print()

# 총 3구역으로 나누고 
# 첫번째 구역은 '-'로 30개, "문자열 곱하기" + "연습"을 출력
# 두번째 구역은 '+'로 50개, "쌍"따옴표"로 강조하기"출력
# 세번째 구역은 '$'로 20개, \n로 줄바꿈 문자열 만들기 "줄바꿈 문자 연습" 출력

print('-' * 30)
print("문자열 곱하기" + "연습")
print('-' * 30)

print()
print()

print('+' * 50)
print("쌍\"따옴표\"로 강조하기")
print('+' * 50)

print()
print()

print('$' * 20)
print("줄바꿈 \n문자 연습")
print('$' * 20)



# 문자열 길이 구하기기
a = "파이썬 수업 진행중"
len(a)
print(len(a))

print(a[0])

# 파업 이라는 글자를 출력해보자 인덱싱 + 슬라이싱

print(a[0] + a[5])