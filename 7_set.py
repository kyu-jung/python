# 집합
s1 = set([1, 2, 3])
print(s1)


# 집합에는 중복을 허용하지 않음.
# 순서가 없어 집합안에서 순서가 바뀌어 출력됨.
s2 = set("Hello")
print(s2)


l1 = list(s1)
print(l1)
print(l1[0])


t1 = tuple(s1)
print(t1)
print(t1[0])



# 교집합 구하기
# 교집합 기호 &
s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])

print(s3 & s4)
print(s3.intersection(s4))
print(s4.intersection(s3))


# 합집합 구하기
# 합집합 기호 |
print(s3 | s4)
print(s3.union(s4))
print(s4.union(s3))


# 차집합 구하기
# 차집합 기호 -
print(s3 - s4)
print(s3.difference(s4)) # 1,2,3
print(s4.difference(s3)) # 7,8,9


# add 한개만 추가
s3.add(7)
print(s3)


# update 여러개 추가
s3.update([10,11,12])
print(s3)


# remove 특정값 제거하기 한개씩만 제거가능
s3.remove(1)
print(s3)


