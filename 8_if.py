# if문
money = True
if money:
    print('택시를 타고 가라')
else:
    print('걸어가라')


if 1>2:
    print('1이 2보다 크다')
else:
    print('1이 2보다 크지않다')

# 비교 연산자
# <,>,==,!=,<=,>=

# !=를 사용해서 값을 비교하여 if문 안의 코드가 작동하도록 만들어봅시다.
if "C#" != "파이썬":
    print('C#과 파이썬은 같지 않다')
else:
    print('C#과 파이썬은 같다.')


# or, and, not
a = True
b = False

if a or b:  # 조건1 or 조건2
    print("a와 b중 하나만 참이어도 참")
if a and b:  # 조건1 and 조건2
    print("a와 b가 모두 참")
if not a:  # not 조건1
    print("a의 부정형")


# in, not in
e = [1,2,3]
f = (4,5,6,)

if 1 in e:
    print('e 리스트 안에 숫자 1 있음')
else:
    print('e 리스트 안에 숫자 1 없음')

if 1 not in f:
    print('f 리스트 안에 숫자 1 없음')
else:
    print('f 리스트 안에 숫자 1 있음')


# 문자열을 만들어서 안에 '문자'가 있는지 확인해보자.
과일 = ['사과', '딸기', '포도', '바나나']

if '바나나' in 과일:
    print('바나나가 있습니다.')
elif '바나나' not in 과일:
    print('바나나 사놓으세요.')
else:
    pass


# 조건문에서 아무 일도 하지 않게 설정하려면 pass사용
# elif 다중조건 필요시 사용
# 개수 제한 없음



# 조건부 표현식
score = 70
message = "success" if score >= 60 else "failure"
print(message)



# if else elif / 비교연산자( >,<,!=,>=,<=) / or, and, not / in, not in


# not (1 > 2) -> True # 틀린것을 부정하므로 참이다.



# 비교연산자 2개, or / (조건1) or (조건2)
if (1 < 2) or (6 != 3):
    print('참이다')
else:
    print('거짓이다')

# not in 리스트 /
g = ['한국', '미국', '스위스','이탈리아']
if '베트남' not in g:
    print('베트남으로 여행가자')
else:
    print('다른나라를 찾아보자') 