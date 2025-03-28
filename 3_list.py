# 리스트의 인덱싱싱
a = [1, 3, 5, 7, 9]
print(a)
print(a[0] + a[2])


# a 리스트에서 2번 인덱스와 4번 인덱스 값을 더해서 출력해보자.
print(a[2] + a[4])
print(a[2] - a[4])
print(a[2] * a[4])
print(a[2] / a[4])



a = [1,2,3, ['a','b','c']]
print(a[0])     # 리스트 안의 첫번째 값
print(a[3])     # 리스트 안의 네번째 값 (리스트 형식) 
print(a[3][1])  # 리스트 안의 네번째 값 속의 값


a = [1,2,['a','b', ['한국','폴리텍']]]
print(a)              # 전체 리스트 값을 출력
print(a[1])           # 전체 리스트에서 1번째 값을 출력
print(a[2])           # 전체 리스트에서 2번째 값 (리스트 형식)
print(a[2][1])        # 전체 리스트 속에 있는 두번째 리스트의 1번째 값을 출력
print(a[2][2][0])     # 전체 리스트 속에 있는 두번째 리스트 속에 있는 세번째 리스트의 0번재 값

print()
# b = [1, ['a', 'b'], 2, ['한국', '폴리텍']]
# 1. ['a', 'b'] 출력하세요
# 2. '한국'을 출력하세요
# 3. 'b'를 출력하세요요
# 4. 2를 출력하세요
b = [1, ['a', 'b', 'c', 'd'], 2, ['한국', '폴리텍', '아산', '캠퍼스']]
print(b[1])
print(b[3][0])
print(b[1][1])
print(b[2])

print(b[-1])



# 리스트의 슬라이싱
print(b[1][1:3])
print(b[3][:3])

# b에서 1번째 요소에 접근하여 'c', 'd'를 출력
# b에서 3번째 요소에 접근하여 '폴리텍', '아산' 출력

print(b[1][2:4])
print(b[1][2:])
print(b[3][1:3])


# 리스트 연산하기
a = [1,2,3]
b = [4,5,6]
print(a + b)
print(a * 2)

print(len(a))
print(len(a + b))
print(len(a * 2))


print(str(a[1]) + 'hi')


# 리스트의 값 수정하기

a[1] = 9
print(a)


# del함수를 사용해 리스트 요소 삭제하기
del a[1]
print(a)