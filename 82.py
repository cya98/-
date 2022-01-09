# 정수 세 개를 입력받고 합계 출력하기
a, b, c = map(int, input('숫자를 세게 입력하세요: ').split())
print(a + b + c)

# 변수 만들기
# 50
# 100
# None 이 각 줄에 출력되게 만드세요

a, b, c = 50, 100, None
print(a)
print(b)
print(c)

# 평균 점수 구하기
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됨, 평균 점수를 구하는 프로그램을 만드세요 단, 평균점수를 출력할 때는 소수점 이하 자리는 버립니다.

korean, english, math, science = map(int,input().split())
print((korean + english + math + science) // 4)

# 값을 여러 개 출력하기
# print에는 변수나 값 여러 개를 ,(콤마) 로 구분하여 넣을 수 있다.
# 콤마로 구분해서 넣으면 각 값이 공백으로 띄어져서 한 줄로 출력된다.
print(a, b, c) # 50 100 None
print(1, 2, 3) # 1 2 3 
print('hello', 'Python') # hello Python

# sep // 공백이 아닌 다른 문자 넣기
print(1, 2, sep='hoho') # 1hoho2
print(1, 2, 3, sep=', ') # sep에 콤마와 공백을 지정 1, 2, 3
print(1, 2, 3, sep=',') # sep에 콤마만 지정 1,2,3
print('Hello', 'Python', sep='') # sep에 빈 문자열을 지정 HelloPython 이렇게 빈 문자열을 지정하면 원래는 공백이 있어서 띄어서 출력되는데 각각 값이 붙어서 출력됨
print(1920, 1080, sep='x') # sep에 x를 지정 1920x1080

# '\n' 줄바꿈 활용하기 # '\n'은 값을 다음 줄에 출력하게 만드는 제어 문자입니다. 따라서 sep에 \n 을 지정하면 줄 바뀌어서 출력 \n 자체는 제어 문자라 화면에 출력x 
print(1, 2, 3) # 1 2 3
print(1, 2, 3, sep='\n') # 1
                         # 2
                         # 3 이렇게 줄이 바뀜 

# 참고로 \n 도 문자이므로 print 에 바로 넣어서 사용할 수 도있음
# \n 은 옆에 다른 문자나 숫자와 붙여서 씀 만약 \n 양옆에 공백을 넣어버리면 공백이 그대로 출력되므로 주의 
# print('1\n2\n3') === print(1, 2, 3, sep='\n') 같은 결과 출력

print('1 \n 2 \n3') #1
                    # 2
                    # 3

# end 사용하기 
# print 는 기본적으로 출력하는 값 끝에 \n을 붙입니다. 그래서 print를 여러 번 사용하면 값이 여러 줄에 출력됨
print(1) # 1
print(2) # 2
print(3) # 3

# 그러면 print를 여러번 사용해서 print(1, 2, 3) 처럼 한줄에 여러 개의 값을 출력할 수는없을까? 이땐 print에 end 에 빈 문자열을 지정해줌됨

# print(값, end='')

print(1, end='') #end 에 빈 문자열을 지정하면 다음번 출력이 바로 뒤에 오게됨
print(2, end='')
print(3)

# 실행결과 123
# end=''와 같이 end 에 빈 문자열을 지정하면 1, 2, 3이 세줄로 출력되지 않고 한줄로 붙어서 출력됨
# 기본적으로 print의 end에 \n이 지정된 상태인데 빈 문자열을 지정하면 강제로 \n 을 지워주기 때문임
# 즉, end는 현재 print가 끝난 뒤 그다음에 오는 print 함수에 영향을 줌 만약123 사이를 띄우고싶으면 end 에 공백 한 칸을 지정하면 됨!

print(1, end=' ') # end에 공백 한 칸 지정
print(2, end=' ')
print(3)

# 실행결과 1 2 3

# 'Hello' 'Python' 을 두 줄로 출력하는 방법
print(3.1, 'Python', 100) # 3.1 Python 100
print(15, 9, sep=':') # 15:9
print('Hello\nPython')
print('Hello', 'Python', sep='\n')
print('Hello', '\n', 'Python', sep='') # sep= '' 을 넣어줘서 두문자열이 붙어서 python이 두번째줄에 공백이 맨앞에 생기지 않도록함

# 날짜와 시간 출력하기 2000/10/27 11:43:59
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':' )

# 날짜와 시간 출력하기 1999-12-31T10:37:21

year = 1999
month = 12
day = 31
hour = 10
minute = 37
second = 21

print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')

year, month, day, hour, minute, second = input().split()
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')