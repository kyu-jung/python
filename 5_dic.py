# 연관배열

# 딕셔너리는 key와 value가 한쌍으로 가지는 자료형

dic = {'이름' : '최규정', '전화번호' : '010-2936-6065', '생일' : '1012'}



print(dic['이름'])
print(dic['전화번호'])


# 딜셔너리 요소 추가하기
high = { '월' : 'plc', '화' : 'C#', '수' : '시퀀스', '목' : '파이썬'}
print(high)

# 변수[키] = 값
high['금'] = 'CAD'
print(high)


# Value에 리스트로 넣을수 있음
day = {'요일' : ['월', '화', '수', '목', '금']}
print(day)
print(day['요일'])



# 변수 명 "rainbow"에 '무지개'가 키, ['빨', '주', '노', '초', '파', '남', '보']가 값
raindow = {'무지개' : ['빨', '주','노', '초', '파', '남', '보']}
print(raindow)

# 다른색 : 검정
raindow['다른색'] = '검정'
print(raindow)


# 변수명 all / 1 : '값' / 'key' : 2 / '자료형' : [3, 'value']
all = {1 : '값', 'key' : 2, '자료형' : [3,'value']}
print(all)
# all 이라는 변수에 'dic' : '사전' 추가하기
all['dic'] = '사전'
print(all)



# 딕셔너리 요소 삭제하기
# del을 사용하려면 해당 값을 지우는 개념이라 list나 dictionary에는 접근이 필요함
# list와 dictionary 접근으로는 변수[인덱스], 변수[키]
# del 변수[키]
del all['dic']
print(all)



# list에 1,2,3,4,5를 넣고 인덱스 2에 있는 값을 지워주세요
숫자 = [1,2,3,4,5]
print(숫자)
print(len(숫자))
del 숫자[1]
print(숫자)
print(len(숫자))


# 리스트 10,20,30,40,50
# 딕셔너리 10 : '10' / 20 : '20' / 30 : '30' / 40 : '40' / 50 : '50'
# 각 변수에서 20과 40을 출력하시오.

b = [10,20,30,40,50]
print(b[1],b[3])
a = {10:'10',20 : '20',30 : '30',40 : '40',50 : '50'}


# 딕셔너리에서 key를 사용해서 value얻기
# print(변수[키])   ->  해당 value
print(a[20], a[40])


# 딕셔너리 주의사항
# 키가 중복일 경우 맨 뒤에 쌍만 인정
c = {1 : 'a', 1 : 'b', 1 : 'c'}
print(c)

# 키로 list는 불가 -> 가변적이어서 안됨
# 키로 tuple은 가능 -> 불변적이어서 가능
# d = {[1,2] : 'hi'}
# print(d)




# key 리스트 만들기

e = {'한국' : '폴리텍', '하이테크' : '반도체장비'}

print(e.keys())  # -> dict_keys(['한국','하이테크'])

# 모아준 key 모음집을 리스트화 하기
print(list(e.keys()))  # -> ['한국','하이테크']

# print(list(e.keys())) 활용법
# 모아준 KEY 모음집을 리스트화 한 것을 활용하기기
f = list(e.keys())  # f = ['한국','하이테크']
print(f[0])   # -> 한국



# value 리스트 만들기
print(e.values())  # -> dict_values(['폴리텍','반도체장비'])
print(list(e.values())) # -> ['폴리텍', '반도체장비']


# items()  dictionary와 내용은 같지만 한 쌍씩 묶어줌
print(e)
print(e.items()) # -> dict_items([('한국','폴리텍'),('하이테크','반도체장비')])
print(list(e.items())) # -> [('한국','폴리텍'),('하이테크','반도체장비')]


# 1교시 : 국어 / 2교시 : 수학 / 3교시 : 영어 / 4교시 : 사회 / 5교시 : 과학
# keys(), values(), items()
# list로 형변환 한것을 다른 변수에 담고 각자 2번 인덱스에 있는 것을 출력해봅시다.

p = {'1교시' : '국어',  '2교시' : '수학' , '3교시' : '영어' , '4교시' : '사회' , '5교시' : '과학'}
print(list(p.keys()))
print(list(p.values()))
print(list(p.items()))

q = list(p.keys())
print(q[2])

w = list(p.values())
print(w[2])

r = list(p.items())
print(r[2])  # 결과값이 튜플의 형태로 나옴 -> ('3교시', '영어')
print(r[2][1]) # 그래서 튜플 안의 결과값을 원할경우 이중 인덱싱 사용 -> 영어

# 변수를 만들때는 자료형 이름을 사용하지 않음. 컴파일러가 오해를 한다.



# clear  딕셔너리 안의 모든 요소를 삭제함.
# p.clear()
print(p)



# 리스트 [], 튜플 (), 딕셔너리 {}
# 리스트는 가변성이 있고 여러 함수를 사용해서 자유롭게 이용가능
# 튜플은 리스트와 비슷하지만 수정,삭제 안됨. 변동이 있으면 안되는 데이터에 사용
# 딕셔너리는 가변성이 있고 여러 함수를 사용하지만 값에 대한 접근성은 순서가 없음. 
# 즉 인덱스가 없고 키로 작용이 됨.


# get
# print(p['0교시']) # 변수[키] 했을때 '없는 키'면 오류
print(p.get('0교시')) # 변수.get(키) 했을때 없는 키면 None을 반환
print(p.get('0교시','수업없음')) # 키가 없을때 원하는 값을 반환 하도록 할 수 있음.


# in  -> 키가 있는지 확인하는 기능 (참, 거짓으로 반환해줌)
print('0교시' in p) # false
print('1교시' in p) # true
