#문자 개수 세기
a = "취미"
a.count("취")
print(a.count("취"))

b = "hobby"
b.count("b")
print(b.count("b"))

# c라는 변수에 banana를 넣고 .count를 a갯수를 반환해봅시다.
c = "banana"
c.count("a")
print(c.count("a"))


# 위치 알려주기 - find
d = "한국 폴리텍 아산 캠퍼스"
print(d.find('폴'))
print(d.find('김'))

# e라는 변수에 "파이썬 수업 진행중" 를 넣고, .find를 사용해서 '업'이라는 글자 위치 반환하기
e = "파이썬 수업 진행중"
print(e.find('업'))



# 위치 알려주기 - index
f = "파이썬 수업 진행중"
print(f.index('업'))

#g = "파이썬 수업 진행중"
# print(g.index('김'))

# g라는 변수에 "오후 1시 수업중"를 넣고 .index를 사용해서 오류 먼저 내보고, "수"라는 글자 위치 변환하기
g = "오후 1시 수업중"
# print(g.index("김"))
print(g.index('수'))



# 문자열 삽입 - join
# 문자열에 넣어줄 "문자".join("문자열")
print(",".join('abcd'))

print("#".join("12345"))

# 문자 "$"를 join해서 문자열 "한국폴리텍"에 넣어줍시다.
print("$".join("한국폴리텍"))



h = "hi"
print(h.upper())  # 소문자를 대문자로 반환해줌, 원본은 바뀌지 않음
print(h)


h = "HI"
print(h.lower())  # 대문자를 소문자로 반환해줌, 원본을 바뀌지 않음음
print(h)


# i라는 변수에 'apple' 을 넣고 대문자 출력하도록 upper 사용
# i라는 변수에 'APPLE' 을 넣고 소문자 출력하도록 lower 사용
i = "apple"
print(i.upper())
i = "APPLE"
print(i.lower())


j = "한국폴리텍 아산캠퍼스 C# 수업중입니다."
print(j.replace("C#","Python"))


# j 변수에 "한국폴리텍 아산캠퍼스 C# 수업중입니다."를 넣고 .replace를 사용해서
# '한국'을 '미국'으로 바꿔줍시다.
print(j.replace('한국','미국'))


# 문자열 나누기
# .split() 괄호 안에 기호나 문자 등 구분자가 없으면 공백을 기준으로 문장을 잘라서 리스트에 담는다.
print(j.split())
