# '반복적으로 사용되는 가치 있는 부분'을 
# 한 뭉치로 묶어 '어떤 입력값을 주었을 때 어떤 결괏값을 리턴해줌'.


# 반환값 있고 매개변수 있음
def add(a,b):
    result = a + b
    return result
print(add(1,2))  # 3을 출력


# 매개변수와 인수
# 매개변수 -> 함수에 임력으로 전달된 값을 받는 변수
# 인수 -> 함수를 호출할 때 전달하는 입력값

# 반환값 있고 매개변수 없음
def say():
    return 'Hi'

print(say())


# 반환값 없고 매개변수 있음
def mul (a,b):
    print("%d X %d = %d" %(a,b,a*b))

mul(1,2)


# 반환값 없고 매개변수 없음
def school():
    print('폴리텍')

school()


print()



# 반환 없고 매개변수 없는 함수
def q():
    print('귤')

q()

# 반환 없고 매개변수 있는 함수
def w(c,d):
    print(c*d)

w(20,5)

# 반환 있고 매개변수 없는 함수
def e():
    return '귤은 맛있다.'

# 반환 있고 매개변수 있는 함수
def r(e,f):
    return e + f
print(r('감','귤'))


print()
# 여러개의 입력값을 받는 함수 만들기    함수이름(*매개변수)
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
    
print(add_many(1,2,3,4,5,6))

print()
def add_mul(opperator,*args): # opperator 자동화  / *를 사용할때는 뒤에 사용하여야 컴퓨터가 알아듣는다.
    if opperator == '+':
        result = 0
        for i in args:
            result += i
    elif opperator == '*':
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul('+', 5,6))
print(add_mul('+', 5,6,10,15))
print(add_mul('*', 5,6,10,15))
print(add_mul('*', 5,6))



# *매개변수는 여러가지 인자를 받는 매개변수이므로 맨 앞에 위치할 경우 단순','로는 구분하기 어렵다.
# 구분되는 매개변수에는 직접 값을 입력해줌 
def add_much(*args, much):
    result = 0
    for i in args:
        result += i
    result += much
    return result

# add_much(1,2,3,4,5)

print(add_much(1,2,3,4,5, much = 3)) # 변수명을 반드시 알고 있어야 지정하여 사용할 수 있다.

print()

 # 키워드 매개변수 kwargs   함수이름(**매개변수)
def keyword(**kw):
     print(kw)
keyword(name = '최규정', school = 'polutech', clsses = '7교시', hours = 3)

 # 반환값이 없는 함수를 출력할 경우 None
print(keyword(name = '최규정', school = 'polutech', clsses = '7교시', hours = 3))



# ** 키워드 매개변수는 맨 앞에 올 수 없다
# 딕셔너리로 변환이 되서 구분을 할 수 없다.
def keyword(word, **kw):
    print(kw)
    return word

print(keyword(123, name = '최규정', school = 'polutech', clsses = '7교시', hours = 3))


print()
# return에 여러값이 들어가나 튜플 한 묶음으로 반환해줌
def add_and_mul(a,b):
    return a+b, a*b, a/b

print(add_and_mul(1,2))

# 변수1, 변수2 = 함수호출 -> 반환값이 여러개이면 각각 변수에 담아줌
result1, result2, result3 = add_and_mul(1,2)

print(result1)
print(result2)
print(result3)


