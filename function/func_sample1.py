# path : function\\func_samply1.py
# module : function.func_samply1

# 파일썬에서 함수 만들어 사용하기
'''
# 구문
def 함수명(매개변수): 
    함수가 실행할 코드 구문들
    .....
     :return 값 또는 변수 또는 값, 값, ... 값 여러개 => 받는 변수는 튜플임.
    
    * 매개변수 (parameter) : 0 ~ n개    
    
# 함수 사용 (호출, function call) 
 : 함수가 만들어진 형태(signature) 에 맞춰서 사용해야 함.
 : 함수 이름 틀리지 않아야 함. (대소문자, _ 갯수 확인)
 : 매개변수의 갯수 일치되게 전달인자(argument) 사용해야 함.
 : 반환값 여부도 확인, 반환값 있는 함수(중첩함수()) 로 사용 가능함.
'''

# 아무런 기능없는 빈 함수 - pass, None 작성
def func():
    pass

# 함수이름 아래에 함수 설명(description) 을 적어둘 수 있음 - 따옴표 사용
def hello():
    '이 함수는 연습용입니다. '
    print('Welcome!')
    print('함수명에 공백, 예약어 사용 못함')

    # 반환값이 없는 리턴은 생략해도 됨.
    return

# 매개변수 있고, 반환값 있는 함수
def add(x, y):
    print(f'{x} + {y} = {x+y}')
    return x+y

# 여러개의 값을 리턴 할 수 있음, 자동 튜플로 처리.
def func2(a,b):
    print(f' a : {a}, b : {b}')
    return a*2, b*2

# # 함수 호출 =========
# if __name__ == '__main__':
#     # hello()
#
#     # 함수 설명(description) 을 확인할 때 help(함수명) 사용
#     # help(hello)
#     # help(input)
#     # help(print)
#
#     # 매개변수 있고 반환값 있는 함수 사용(call)
#     # total = add (10,20)
#     # print(f'{total}')
#     #
#     # total = add (10.5,20.9)
#     # print(f'{total}')
#     #
#     # result = add('a','b')
#     # print(f'{result}')
#
#     result = func2(10,20)
#     print(f'{result}', type(result))
#
#     n1, n2 = func2(10,20)
#     print(f' n1 : {n1}, n2 : {n2}', type(n1), type(n2))

# -------------------------------
# 변수 생성과 사용 영역 (지역, 스코프 scope)
# 지역변수 (local variable) 와 전역변수 (global variable)
def func1():
    num = 10    # 함수안에서 만들어진 변수 : 지역변수
    print(f'지역변수 num : {num}')

num = 100    # 전역변수
def func_global():
    # print(f'전역변수 num : {num}')  # 전역변수 다음 위치에서는 어디서나 사용 가능
    
    # global 을 선언하지 않으면 지역변수임.
    global num
    num = 200
    print(f'global 선언으로 전역변수 100 에서 전역변수 num : {num} 으로 변경됨')

# 함수의 매개변수 ( parameter) 는 전달받은 값을 변경할 수 없다.
# 단, 전달받은 값이 군집자료형일 때는 아이템(요소)는 변경할 수 있음.
def list_func(plist):
    print('     plist 가 받은 주소 : ', id(plist))
    print('     전 : ', plist)
    plist[1] = 10
    print('     후 : ', plist)

# 함수 밖에서 지역변수 사용 못함
if __name__ == '__main__':
    # func1()
    # func_global()
    # print(f'전역변수 num : {num}')

    list1 = [1,2,3]
    print('list1 주소 : ', id(list1))
    print('list1 : ', list1)
    list_func(list1)
    print('list1 : ', list1)
    
    
    