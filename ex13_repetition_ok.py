# 반복문
'''
for 변수 in range(횟수):
     반복할 코드
'''

# range는 연속된 숫자를 생성
# range는 0~99까지 생성을 의미
for i in range(100):
    print('Hello, world! %d' % i)

# 시작하는 숫자와 끝나는 숫자 지정
for i in range(2,10): #2부터 9까지
    print(i)


print("----------------")
# 증가폭 사용
# 시작하는 숫자와 끝나는 숫자 지정
for i in range(2,10, 2): #2부터 9까지 2씩증가
    print(i)
    


print("----------------숫자 감소")
# 숫자 감소
for i in range(10, 0, -1):
    print(i)
    
# for 변수 in reversed(range(횟수))
# for 변수 in reversed(range(시작, 끝))
# for 변수 in reversed(range(시작, 끝, 증가폭))
for i in reversed(range(10)):
    print('Hello, world!', i)
    
# 시퀀스 객체 반복
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for i in fruits:
    print(i)
    
for letter in reversed('Python'):
    print(letter, end='')
    
################################
# while문 사용
'''
초기식
while 조건식:
     반복할 코드
     변화식
'''
# while문 작성
i = 0                     # 초기식
while i < 100:            # while 조건식
    print('Hello, world!', i)    # 반복할 코드
    i += 1                    # 변화식

# while문 초기값 감소
i = 100
while i > 0:
    print('Hello, world!', i)
    i -= 1
