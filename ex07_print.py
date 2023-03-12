# print는 출력할 값을 ,(컴마)로 구분할 수 있음
# 컴마 사이에 공백이 생
print(1, 2, 3)
print('Hello', 'Python')

#sep(separator) 출력값 사이 문자 넣
print(1, 2, 3, sep=', ')    # sep에 콤마와 공백을 지정
print(4, 5, 6, sep=',')    # sep에 콤마만 지정
print('Hello', 'Python', sep='')    # sep에 빈 문자열을 지정
print(1920, 1080, sep='x')    # sep에 x를 지정