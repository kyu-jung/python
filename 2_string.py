# 문자열을 표현할때는 '', ""로 표현한다.
"Hello World"
'Python'
print("Hello World")
print('Python')


# 여러줄을 주석할때 사용한다.
"""Asan Politech"""
'''Politech Asan'''

print("안녕하세요. '최규정'입니다.")
print('안녕하세요."아산캠퍼스"입니다.')




# 문자열에서 일부분 강조하여 표현하기
# ''로 강조하여 교수님 '수업'마쳐주세요. 를 출력해봅시다.

print("교수님 '수업'마쳐주세요.")

# ""로 강조하여 교수님 "수업"마쳐주세요. 를 출력해봅시다.

print('교수님 "수업"마쳐주세요.')


# 같은 기호로 작성하면 오류가 날 수 있다.
# print("교수님 "수업"마쳐주세요.")


# 같은 기호로 작성하고 싶을때는 역슬래시를 이용하면 표현할 수 있다.
print('Python \'재미있습니다.\'')
print("Python \"재미있습니다.\"")


multiline = "오늘은 파이썬 \n 수업하는 날"
print(multiline)

multiline2 = '''지금은 
여러줄 만드는 연습'''

print(multiline2)

multiline3 = """큰따음표
연습하는 중




"""

print(multiline3)


# 다음 문장을 \n과 """, '''를 이용하여 여러줄 출력을 해봅시다.
# 지금은 여러줄 문자열을 만드는 연습을 하고 있습니다.

print("지금은 여러줄 문자열을 \n 만드는 연습을 하고 있습니다.")

multiline4 = """지금은 여러줄 
문자열을 만드는 연습을 하고
있습니다."""
print(multiline4)

multiline5 = '''지금은 여러줄 문자열을 
만드는 연습을 하고 
있습니다.'''
print(multiline5)


# 이스케이프 코드 *참고만
print("탭연습을\t합니다.")
print("이거 허\\용해줌")
print("이거 허\a용해줌")
