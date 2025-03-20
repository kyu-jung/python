# append
a = [1,2,3]
a.append(4)
a.append("a")
a.append(["한국", "폴리텍"])
print(a)


# sort
a = [4,4,5,5,1,1,8,8,3,3]
a.sort()   # 오름차순으로 정렬후 원본에 적용
print(a)


# reverse
a.reverse()  # 역순으로 나열
print(a)


print(a.index(3))


# insert 리스트에 요소 삽입
a.insert(1,9)
print(a)



# remove  리스트에 요소 제거
a.remove(3)
print(a)



# pop  리스트 요소 끄집어내기
# 맨 마지막 요소를 반환 후 삭제함 / ()괄호안에 원하는 순번의 요소 입력시 그 순번의 요소 반환 후 삭제함
a.pop()
print(a.pop()) # 꺼낸 값을 print라는 함수로 출력만 함
print(a)       # pop을 통해서 맨끝에 있던 값이 삭제된 리스트 a를 출력 한 것

# pop()은 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제한다.
# pop(x)는 리스트의 x번째 요소를 리턴하고 그 요소는 삭제한다.

a.pop(1)
print(a.pop(1))
print(a)


# count    .count(값) 값이 몇개인지 세준다. 없으면 0으로 표현현
print(a.count(8))
print(a.count(4))
print(a.count(0))



# extend
a.extend([10, 15])

a = a + [10, 15]
a += [10, 15]


print(a)



# 리스트의 값을 추가하는 방법에는 append, insert, extend, +, +=가 있는데
# append(값) 리스트와 상관없이 맨끝에 값을 추가하는 내용이었습니다.

# a = [1,2,3]
# .append를 이용해서 '한국', '폴리텍', 5, 6을 넣어보자.
a = [1,2,3]
a.append('한국')
a.append('폴리텍')
a.append(5)
a.append(6)

print(a)

# .append를 이용해서 ['리스트1', '리스트2', 3, 4]를 넣어보자
# a.append(['리스트1', '리스트2', 3, 4])
# print(a)

# insert를 이용해서 3번째에 있는 위치에 '파이썬'이라는 값을 넣어봅시다.
a.insert(3, '파이썬')

print(a)


# pop을 이용해서 2번째에 위치한 값을 뽑아내고, pop을 이용해서 맨끝에 위치한 값을 뽑아서 사칙연산 해봅시다.
# 뽑아낸 값이 없어지기 때문에 임의의 변수를 설정하여 사칙연산 한다.
b = a.pop(2)
c = a.pop()

print(b + c)
print(b - c)
print(b * c)
print(b / c)


# .extend를 사용해서 ['마지막', '수업','시간']를 추가
a.extend(['마지막', '수업','시간'])
print(a)


# +를 사용해서 리스트 합체하기
# a = [1,2,3] b = [1,2] / a와 b 리스트를 합쳐보자
a = [1,2,3]
b = [1,2]
print(a + b)


# += 를 사용해서 리스트 합체하기
# 리스트 [4,5]를 a에 넣어줍시다.
a += [4,5]
print(a)


# 리스트 c = [6,4,6,8,2,4,1,6,7]
# 리스트를 내림차순으로 정렬해봅시다.
c = [6,4,6,8,2,4,1,6,7]
c.sort()
c.reverse()
print(c)


# 리스트 d = [1,1,1,2,2,2,5,5,5,7,7,7,9,9,9]
# remove를 통해서 숫자5 하나를 지워주세요
# count를 이용해서 숫자 5가 지워졌는지 확인하고 리스트 d를 출력해봅시다.
d = [1,1,1,2,2,2,5,5,5,7,7,7,9,9,9]
d.remove(5)
print(d.count(5))
print(d)

