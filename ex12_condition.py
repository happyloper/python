# 조건문
# 조건이 충족때 실행
'''
if 조건식:
     코드
'''

# if문 다음 줄에서 들여쓰기 필수
x = 10
if x == 10:
    print("10입니다.")

# 조건문 코드 생략 pass
x = 10
if x == 10:
    pass  # TODO: 이후에 처리 하자

# if 조건문 들여쓰기
# if 다음에 오는 코드들은 반드시 들여쓰기 깊이가 같아야 함
# :가 나오면 그 다음 줄부터는 무조건 들여쓰기
x = 10

if x == 10:
    print('x에 들어있는 숫자는')
    print('10입니다.')

# if문 작성
x = 15

if x >= 10:
    print('10 이상입니다.')
    if x == 15:
        print('15입니다.')
    if x == 20:
        print('20입니다.')

x = 3
if 3 > 2:
    print("2보다 3이 크다")
    if x == 1:
        print("1과 같다")
    if x == 3:
        print("3과 같다")

# 입력값 받아서 조건문 처리
'''
x = int(input())          # 입력받은 값을 변수에 저장
if x == 10:               # x가 10이면
    print('10입니다.')    # '10입니다.'를 출력
if x == 20:               # x가 20이면
    print('20입니다.')    # '20입니다.'를 출력
'''
#####################
# if else 문 사용
'''
if 조건식:
     코드1
else:
     코드2
'''

# else: 다음도 들여쓰기를 맞춰 주어야 함
x = 5
if x == 10:
    print("10입니다.")
else:
    print("10이 아니다.")

# if else none
if True:
    print('참')    # True는 참
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')    # False는 거짓

if None:
    print('참')
else:
    print('거짓')    # None은 거짓

'''
# 값 자체가 있으면 if는 동작
# 0, None, ''은 False로 취급
'''
# if 조건문 숫자 지정
if 0:
    print('참')
else:
    print('거짓')    # 0은 거짓

if 1:
    print('참')    # 1은 참
else:
    print('거짓')

if 0x1F:    # 16진수
    print('참')    # 0x1F는 참
else:
    print('거짓')

if 0b1000:    # 2진수
    print('참')    # 0b1000은 참
else:
    print('거짓')

if 13.5:    # 실수
    print('참')    # 13.5는 참
else:
    print('거짓')

# if 조건문에 문자열 지정
if 'Hello':    # 문자열
    print('참')    # 문자열은 참
else:
    print('거짓')

if '':    # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓

# 다중조건
x = 10
y = 20

if x == 10 and y == 20:     # x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')

# 중첩 IF문
if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')

# 중첩 if문은 and 논리 연산자 사용
if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')

# elseif 사용
'''
if 조건식:
     코드1
elif 조건식:
     코드2
'''
x = 20
if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')

# if, elseif, else 모두 사용
'''
if 조건식:
    코드1
elif 조건식:
    코드2
else:
    코드3
'''
x = 30

if x == 10:             # x가 10일 때
    print('10입니다.')
elif x == 20:           # x가 20일 때
    print('20입니다.')
else:                   # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.')
