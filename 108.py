# 여러 줄로 된 문자열 사용하기

hello = '''hello, world 
안녕하세요.
Python입니다.'''

print(hello) # hello, world
             # 안녕하세요.
             # Python입니다.
             
# 그런데 왜 ''' 와 """ 둘중 하나로 통일 하지 않고 여러가지 방식을 사용할까?

# 문자열 안에 작은따옴표나 큰따옴표 포함하기

# 문자열안에 ' 를 사용하고 싶으면 " " 로 묶어주기
# 문자열안에 " 를 사용하고 싶으면 '로 묶어주기
# 문자열안에 ', " 둘다 사용하고 싶으면 """ 나 ''' 로 묶어주면됨

# 혹은 작은따옴표 안에 작은 따옴표 를 넣는 방법이 아예 없을까?  x
# 작은 따옴표 앞에 역슬래시\를 넣어주면됨

print('Hi, he isn\'t bad')

print(""""Hello", World""")

# 연습 문제 여러 줄로 된 문자열 사용하기

s = """Python is a programing languge that lets you work quickly
and 
integrate systems more effectively."""
print(s)

# 연습 문제

s ="""Python is a "programing languge"
that lets you work quickly
and 
integrate systems more effectively."""

print(s)

# 리스트와 튜플 사용하기

# 지금까지 변수에는 값을 한 개씩 저장함
# 그럼 값을 30개 저장하려면 어떻게 할까 하나하나 다 치는게아니라 리스트를 활욜하면된다

a = [38, 45, 87, 45, 44]
print(a) # [38, 45, 87, 45, 44]
# 이 리스트 안에 있는 값들을 요소(element) 라고 부름

# 리스트에 여러 가지 자료형 저장하기

# 리스트는 문자열, 정수, 실수, 불 등 모든 자료형을 저장할 수 있으며 자료형을 섞어서 저장해도 됨

person = ['james', 23, 180.1, True]
print([person])


# 이렇게 리슽츠에 여러가지 자료형을 사용하면

