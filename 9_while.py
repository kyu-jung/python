treeHit = 0

# 조건에 비교연산자(>,<,>=,<=,!=,==) 사용
while treeHit < 10:
    treeHit += 1 # treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다.')


# 5번 반복하는 반복문을 만들어 봅시다.
사과 = 0
while 사과 < 5:
    사과 += 1 
    print("사과를 %d번 먹었습니다." % 사과)
    if 사과 == 5:
        print('사과가 없습니다.')


# while 문 만들기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: 
"""

number = 0
while number != 4:  # number == 4일때 종료
    print(prompt)
    number = int(input())


# while문 강제로 빠져나가기
# 참이면 계속 돌아간다. break를 만나면 종료한다.
number2 = 0
while True:  
    print('출력합니다.')
    if number2 == 10:
        break


# while문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a += 1
    if a % 2 == 1 : 
        continue
    print(a)


