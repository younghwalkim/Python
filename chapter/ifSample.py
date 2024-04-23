# path 표현 : chapter\\ifSample.py
# module 표현 : chapter.ifSample

# 제어문(조건문) : if , if else, if elif else 문 사용테스트 스크립트
'''
제어문 종류 :  조건문(if), 반복문(loop), 분기문
조건문(if) : if 문, if else 문, if elif else 문
반복문(loop) : for 문, while 문
분기문 : continue 문, break 문
'''

# 조건문에서는 조건식(표현식:expression) 작성이 중요!!
# 조건표현식(계산식)은 반드시 결과가 참 또는 거짓이 나오도록...

# 조건문 작성형식 1 : if 문
def test_if1():
    if(True):
        print('if 조건이 참이면 실행됨.')

    print('if 종료되고 나서 실행 되는 구문임')

    if False:
        print('if 조건이 참이면 실행됨.')
        
    print('if 종료되고 나서 실행 되는 구문임')

def test_if2():
    num = int(input('정수 숫자 입력 : '))
    if (num == 1) :
        print('num : ', num, type(num))
    else :
        print('입력값은 1이 아님 :  ', num, type(num))

def test_even_add():
    num = int(input('정수 숫자 입력 : '))
    if (num % 2 == 0) :
        print('짝수 even : ', num, type(num))
    else :
        print('홀수 add : ', num, type(num))

def test_range():
    num = int(input('정수 숫자 입력 : '))
    if(num >=  1 and num <= 100 ):
        print(f'{num}의 제곱값 : {num**2}')
    else :
        print('1~100 사이의 숫자를 입력하시오.')

# in 연산자 : 군집자료형 (list, tuple, set, dict, str) 에 사용함
# 변수 또는 값 in 군집자료형변수
def test_in():
    print(2 in [1,2,3])
    print(2 not in [1, 2, 3])
    print('a' in 'abcde')
    print('a' not in ('a','b','c'))

def checkPayment1():
    payment = ['card','money','mobile']
    price = 5000

    if 'money' in payment:
        print(f'{price}원을 현금 지불하였습니다. ')
    else :
        print('다른 결제 수단을 선택하세요.')

# 다중 if 문
# if .. elif .. elif ...[else]
def checkPayment2():
    payment = ['결제수단', 'card','money','mobile','zeropay']

    print('==결재수단선택==')
    print('1. 카드')
    print('2. 현금')
    print('3. 모바일')
    print('4. 제로페이')

    no = int(input('결제수단 번호 입력 : '))
    price = int(input('결재할 금액 : '))

    if no == 1:
        print(f'{price}원을 {payment[1]} 지불하였습니다. ')
    elif no == 2:
        print(f'{price}원을 {payment[2]} 지불하였습니다. ')
    elif no == 3:
        print(f'{price}원을 {payment[3]} 지불하였습니다. ')
    elif no == 4:
        print(f'{price}원을 {payment[4]} 지불하였습니다. ')
    else :
        print('다른 결제 수단을 선택하세요.')

# 중첩 if 문
def multi_if():
    n1 = 10
    n2 = 20

    if n1 == 10:
        print(f'n1 : {n1}')
        if n2 == 20:
            print(f'n2 : {n2}')
        else :
            print('n2는 20이 아니다.')
    else :
        print('n1 은 10이 아니다.')

# 간단 if 문
# 변수 = 참일때 실행값 if 조건식 else 거짓일 때 실행값
def shortCondition1():
    a = 1
    message = 'a is 1' if a == 1 else  'a is not 1'
    print(message)

def shortCondition2():
    score = int(input('점수 입력 : '))
    message = '합격' if score >= 60 else  '불합격'
    print(message)








