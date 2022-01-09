# input 함수 // 매번 다른 값을 변수에 할당 할때

x = input()
print(x)


a = int(input('첫 번째 숫자를 입력하세요')) #int 로 10 ,20 더해서 30이 되도록 안그러면 1020이 뜸
b = int(input('두 번째 숫자를 입력하세요'))
print(a + b)

#입력 값을 변수 두개에 저장하기

a, b = input('문자열 두 개를 입력하세요').split()
print(a)
print(b)

a, b = input('숫자 두 개를 입력하세요: ').split()

print(a + b)

# 입력 값을 정수로 변환하기
a, b = input('숫자 두 개를 입력하세요: ').split()

a = int(a) #int 에 변수를 넣은 뒤 다시 변수에 저장 int(a)만 입력하면 안돼고 a = int(a) 처럼 변수를 저장 해줘야함
b = int(b)

print(a + b) # 혹은 print(int(a) + int(b)) 이렇게 print 안에서 int 로 변수 변환 하고 바로 더해도 상관없음

# map // split 의 결과를 매번 int로 변환하기 귀찮다, map 에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환 해줌

a, b = map(int, input('숫자 두 개를 입력하세요: ').split())

print(a + b)


