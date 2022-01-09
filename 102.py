# 논리 연산자와 비교 연산자를 함께 사용하기
print(10 == 10 and 10 !=5) # True and True , True
print(10 > 5 or 10 < 3) # True or False , True
print(not 10 > 5) # not True , False
print(not 1 is 1.0) # not False , True

# 비교 연산자로 비교한 결과를 논리 연산자로 다시 판단, 비교연산자(is, is not, ==,!=,>,<, >=, < =) 를 먼저 판단하고 논리 연산자(not, and, or)를 판단

# bool / 정수, 실수, 문자열을 불로 만들기
# 정수, 실수, 문자열을 불로 만들 때는 bool을 사용하면 됨 이때 정수1은 True, 0은 False임.
# 만약 문자열의 내용이 'False' 라도 불로 만들면 True임. 문자열 내용 자체는 판단하지 않고 값이 있으면 True.
# 즉, 정수 0, 실수 0.0 이외의 모든 숫자는 True임. 그리고 빈 문자열 '', "" 를 제외한 모든 문자열도 True.

print(bool(1)) # True
print(bool(0.0))# False
print(bool(6436347)) # True
print(bool('False')) # True 
print(bool('anything'))# True

# 단락 평가
# 논리 연산에서 중요한 부분이 단락평가(short-circuit evalution). 단락 평가는 첫 번째 값만으로 결과가 확실할때 두 번째 값은 확인하지 않는 방법.
print(False and True) # 첫 번째 값이 거짓 이므로 두 번째 값은 확인 하지 않고 바로 거짓으로 결정 False.
print(False and False)# 첫 번째 값이 거짓 이므로 두 번째 값은 확인 하지 않고 바로 거짓으로 결정 False.

# 첫 번째 값이 True 이므로 바로 참 둘중 하나만 True 여도 True 이기 때문에
print(True or True) 
print(True or False)

# 그럼 True 랑 False 끼리 논리 연산자로 확인하면 True 나 False가 나왔는데 True and 'python' 같은건 어떻게 나올까?
print(True and 'python') # 'python' 이 나온다 왜냐하면 파이썬에서는 논리 연산자를 하면 마지막으로 단락 평가를실시한 값을 반환하기 때문,
# 따라서 and 연산자기 때문에 첫 번째 값이 True 기 때문에 두번 째도 확인을 해야 해서( 두번째가 False 일 수도 있으니) 두번 째 'python'을 마지막으로
# 단락 평가 했기 때문에 'python'을 출력한 것 'python'이 True 이기때문에 True를 출력할 것 같지만 그대로 값 그대로를 출력하기 때문에 'python'

# 앞 'python' 이 True 라고 판단하고 두번째 값 까지 확인 하므로 두번째 값이 그대로 출력됨
print('python' and True) # True 
print('python' and False) # False 

# 첫 번째 값이 False, 0 도 False 이기 때문에 첫 번째 값만 확인하고 마지막 단락평가가 첫 번째 값이 기 때문에 첫 번째 값 그대로 출력함
print(False and 'python') # False
print(0 and 'python' ) # 0

# or 연산자도 마찬가지로 마지막 단란 평가를 실시한 값이 반환됨, 첫 번째 값만으로 결과가 결정되므로 첫 번째 값이 반환 됨
print(True or 'python') # True
print('python' or True) # 'python'

print(False or 'Python') # 'Python'
print(0 or False) # False  # 첫 번째 확인하고 두번 째 까지 확인 함으로 두 번째 값인 False 가 출력 됨

# 연습문제 : 합격 여부 출력하기
# 국어,영어, 수학, 과학 점수가 있을 때 한 과목이라도 50점 미만이면 불합격이라고 정했습니다. 합격이면 True 불합격 이면 False가 출력되게 만드세요.


# 4 과목 점수를 입력 했을때 한 과목이라도 50점이 안넘으면 Fasle 아니면 True 를 출력하는 코드
korean, english, mathematics, science =map(int, input('4 과목 시험 점수를 입력 하세요').split())
print(korean >= 50 and english >= 50 and mathematics >= 50 and science >=50 )


korean = 92
english = 47
mathematics = 86
science = 81

print(korean >= 50 and english >= 50 and mathematics >= 50 and science >=50 )


# 국어는 90점이상 영어는 80점 초과 수학은 85점 초과 과학은 80점 이상 일때 합격
korean, english, mathematics, science =map(int, input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >=80 )