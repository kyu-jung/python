test = [1,2,3]

for i in test:
    print(i)


# 다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]
for (num1,num2) in a:
    print(num1 + num2)



# for문의 응용
# for 변수 in 리스트 (또는 튜플 또는 문자열)
score = [10,20,30,40,50]
grade = 0
for scr in score:
    grade += 1
    if scr >= 40:
        print('%d 학점 부여' %grade)
    elif scr >= 30:
        print('중간 점수 부여')
    elif scr >= 20:
        continue  # 해당 코드 건너뛰고 반복문 시작점으로 돌아감
    else:
        print('%d 학점을 받지 못함'%grade)


# range 함수
# range(10)은 0부터 10미만의 숫자를 포함하는 객체

add = 0
for i in range(1,10):
    add += i
    print(add)


# for와 range를 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d" %(i,j,i*j))
    print('')


# 리스트 컴프리헨션
# result = [반복문에 실행된 값 / for num in a]
# [표현식 / for 항목 in 반복_가능_객체 if 조건문]

