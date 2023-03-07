# 반복문 제어
# break, continue문
# break == 제어흐름을 중단하고 빠져나옴
# continue == 반복을 유지한 상태에서 코드의 실행만 건너뜀 

'''
break: 제어흐름 중단
continue: 제어흐름 유지, 코드 실행만 건너뜀
'''

# while문에서 break로 반복문 끝내기
i = 0
while True:    # 무한 루프
    print(i)
    i += 1          # i를 1씩 증가시킴
    if i == 3:    # i가 100일 때
        break       # 반복문을 끝냄. while의 제어흐름을 벗어남
print("-------------------")
# for문에서 break로 반복문 끝내기
for i in range(10000):    # 0부터 9999까지 반복
    print(i)
    if i == 5:    # i가 100일 때
        break       # 반복문을 끝냄. for의 제어흐름을 벗어남

# for문에서 continue로 코드 실행 건너뛰기
for i in range(100):   # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:     # i를 2로 나누었을 때 나머지가 0면 짝수
        continue       # 아래 코드를 실행하지 않고 건너뜀
    print(i)

# while문에서 continue로 코드 실행 건너뛰기
i = 0
while i < 100:    # i가 100보다 작을 때 반복. 0부터 99까지 증가하면서 100번 반복
    i += 1        # i를 1씩 증가시킴
    if i % 2 == 0:# i를 2로 나누었을 때 나머지가 0이면 짝수
        continue  # 아래 코드를 실행하지 않고 건너뜀
    print(i)
    
# 반복문과 pass
for i in range(10):    # 10번 반복
    pass               # 아무 일도 하지 않음

while True:    # 무한 루프
    pass       # 아무 일도 하지 않음