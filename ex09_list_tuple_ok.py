# list는 저장된 요소를 변경, 추가, 삭제 가능

# 리스트 생성
# 여러개의 값을 다룰 때 사용
# 리스트 = [값, 값, 값]
a = []
b = list()

# range 사용 리스트 생성
# range에서 마지막 숫자는 포함되지 않음
# range(횟수)
print("횟수====================")
print(range(10))
# range(시작숫자,총 갯수)
print("시작숫자,총 갯수 ====================")
print(list(range(5,15)))
print("시작숫자,총 갯수, 증가폭====================")
# range(시작숫자,총 갯수, 증가폭)
print(list(range(5, 15, 3)))
print("시작숫자,총 갯수, 감소폭====================")
# range(시작숫자,총 갯수, 감소폭)
print(list(range(10, 0, -1)))

# 리스트의 기본 형식
my_list = [1,3,7,5,2]
print(my_list)

# 리스트의 여러 사용
a = [] # 빈 리스트
b = [1, 2, 3] # 숫자 값
c = ['Life', 'is', 'too', 'short'] # 문자 값
d = [1, 2, 'Life', 'is'] # 숫자,문자
e = [1, 2, ['Life', 'is']] # 숫자, 리스트 포함

# 리스트의 인덱싱
print(b[0])
print(b[0]+b[1])
print(b[-1]) # 마지막 요소 값

##################################
# tuple는 저장된 요소를 변경, 추가, 삭제 불가(읽기전용 리스트)

# 튜블의 생성
# 튜플 = (값, 값, 값)
# 튜플 = 값, 값, 값
a = (38, 21, 53, 62, 19)
print(a)

# 여러 자료형 섞기 가능
person = ('james', 17, 175.3, True)
print(person)

# range 사용 튜플 생성
# 튜플 = tuple(range(횟수))
a = tuple(range(10))
print(a)
# 튜플 = tuple(range(시작, 끝))
b = tuple(range(5, 12))
print(b)
# 튜플 = tuple(range(시작, 끝, 증가폭))
c = tuple(range(-4, 10, 2))
print(c)

# 튜블 -> 리스트 변환
a = [1, 2, 3]
a = tuple(a)
print(a)

# 리스트 -> 튜플 변환
b = list(a)
print(b)