# return의 다른 쓰임새
# 특별할 상황일때 함수를 빠져나가고 싶다면 단독으로 써서 함수를 즉시 빠져나갈 수 있음.
# 함수 내에서 return을 만나면 값이 있으면 반환하고 없으면 함수 탈출. break의 역할을 함.
def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s 입니다.' %nick)

say_nick('수업')
say_nick('보바')
say_nick('비보')
say_nick('바보')


print()

# 매개변수에 초기값 미리 설정하기
def say_myself(name, age, man = True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d 입니다." %age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself('최규정', 20)
say_myself('최규정', 20, False)


print()
# 함수 안에서 함수 밖의 변수를 변경하는 방법
# return
a = 1
def test(a):
    a += 1
    return a

print(test(a))



# global
def test2():
    global a
    a += 1

test2()
print(a)



# lambda
# 함수 이름 = lambda 매개변수1, 매개변수2, ... : 실행문문
# def 와 동일한 역할을 함. 함수를 한줄로 간결하게 만들때 사용
add = lambda b,c : b + c
print(add(3,4))


