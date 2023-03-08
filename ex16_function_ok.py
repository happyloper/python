# 함수
'''
def 함수이름():
     코드
'''     
# 함수를 만들기 전에 함수를 먼저 호출하면 안 된다

# 함수의 실행 순서
# 1. 파이썬 스크립트 최초 실행
# 2. hello 함수 호출
# 3. hello 함수 실행
# 4. print 함수 실행 및 'Hello, world!' 출력
# 5. hello 함수 종료
# 6. 파이썬 스크립트 종료

def hello():
    print('Hello, world!')
hello()

# 빈 함수 만들기
def hello():
    pass

# 매개변수 값 받는 함수
'''
def 함수이름(매개변수1, 매개변수2):
    코드
'''

def add(a, b):
    print(a + b)
add(10, 20)

# 함수 독스트링(documentation strings, docstrings) 사용
'''
파이썬에서는 함수의 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개)로 문자열을 입력하면 함수에 대한 설명을 넣을 수 있습니다. 이런 방식의 문자열을 독스트링(문서화 문자열, documentation strings, docstrings)이라고 합니다. 단, 독스트링의 윗줄에 다른 코드가 오면 안 됩니다.
'''
'''
def 함수이름(매개변수):
    """독스트링"""
    코드
 
def 함수이름(매개변수):
    """
    여러 줄로 된 
    독스트링
    """
    코드
'''

# 함수에서 독스트링 사용
def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    return a + b
 
x = add(10, 20)       # 함수를 호출해도 독스트링은 출력되지 않음
print(x)
 
print(add.__doc__)    # 함수의 __doc__로 독스트링 출력

# 함수 결과 값 반환
'''
def 함수이름(매개변수):
    return 반환값
'''

def add(a, b):
    return a + b
print(add(10,20))

def not_ten(a):
    if a == 10:
        return
    print(a, '입니다.', sep='')
not_ten(5)
not_ten(10)

# 함수에서 여러 개 값 반환
'''
def 함수이름(매개변수):
    return 반환값1, 반환값2
'''

def add_sub(a, b):
    return a + b, a - b

x, y = add_sub(10, 20)
print(x)
print(y)

# 함수에 위치 인수와 키워드 인수 사용

# 위치 인수 사용
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
print(10, 20, 30)

# 언패킹 사용
# 리스트 또는 튜플 앞에 *붙여서 함수에 넣어줌

# 함수(*리스트)
# 함수(*튜플)
x = [10, 20, 30]
print_numbers(*x)

# 키워드 인수 사용
# 함수(키워드=값)

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30, '서울시 용산구 이촌동')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

# 딕셔너리를 키워드 인수로 넣
# 함수(**딕셔너리)
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)

print("=======================")
# **를 두 번 사용하는 이유
# *을 한번 넣으면 x의 키가 출력 == 키를 사용한다는 의미
personal_info(*x)
print("딕셔너리 언패킹 =======================")
personal_info(**x)

# 키워드 인수를 사용하는 가변 인수 함수 만들기
# 매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 keyword arguments를 줄여서 kwargs로 사용합니다. 특히 이 kwargs는 딕셔너리라서 for로 반복할 수 있습니다.
print("=======================")
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

personal_info(name='홍길동')
print("=======================")
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

##############################
# 함수 매개변수에 초기 값 설정
'''
def 함수이름(매개변수=값):
    코드
'''    

def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
    
personal_info('홍길동', 30)
personal_info('홍길동', 30, '서울시 용산구 이촌동')

#매개변수의 초깃값을 지정할 때 한 가지 주의할 점이 있습니다. 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없습니다. 
'''
>>> def personal_info(name, address='비공개', age):
...     print('이름: ', name)
...     print('나이: ', age)
...     print('주소: ', address)
...
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
'''

