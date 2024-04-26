# path : function\\func_samply2.py
# module : function.func_samply2
# 파이썬의 함수 정의(만들기)와 함수 호출(사용) 연습

def tmax(a,b):
    '두개의 값을 전달받아서, 큰값을 리턴하는 함수'
    print(f'a:{a}, b:{b}, type:{type(a)}, type:{type(b)}')
    if a > b:
        return a
    else:
        return b

def func_param_args():
    '매개변수와 전달인자 갯수 일치 테스트용 함수'
    result = tmax(10,20)
    print(f'큰 값 : {result}')
    print(f'큰 값 : {tmax(44.5,12.3)}')
    print(f'큰 값 : {tmax("M","m")}')
    print(f'큰 값 : {tmax(120, 10.3)}')

    # result = tmax(10)
    # result = tmax(10, 20, 30)

def tmax2(a,b):
    '두개의 값을 전달받아서, 큰값을 리턴하는 함수'
    print(f'a:{a}, b:{b}, type:{type(a)}, type:{type(b)}')

    max_value = 0
    if a > b:
        max_value = a
    else:
        max_value = b
    return max_value

def func_call_value():
    '함수로 값 전달 테스트용 함수'
    a = 10
    b = 20
    print(f'a:{a}, b:{b}, type:{type(a)}, type:{type(b)}')

    result = tmax2(a, b)
    print(f'큰값:{result}')

# -------------------------------------

# 파이썬에서는 군집자료형으로 전달받는 매개변수는 주소를 받는다.
def list_in_max(plist):
    '리스트 객체를 전달받아서, 저장된 값들 중 가장 큰 값을 찾아내서 리턴함.'
    print(f'    plist : {plist},  주소 : {id(plist)}')

    max = plist[0]      # 비교의 시작값 지정
    for item in plist:
        if item >  max:
            max = item

    # 전달받은 주소 위치에 각 요소의 값들을 변경 처리
    plist[0] = 1000
    print(f'    plist : {plist},  주소 : {id(plist)}')

    return max

def func_call_address():
    '함수에 주소 전달 테스트용 함수'
    nlist = [45, 1, 33, 12, 90, 123, 7]
    print(f' nlist : {nlist},  주소 : {id(nlist)}')
    result = list_in_max(nlist)
    print(f'큰값 : {result}')
    print(f' nlist : {nlist},  주소 : {id(nlist)}')

# --------------------------------
# 기본 매개변수
'''
# def 함수명(매개변수=기본값, 매개변수=기본값):
    => 주의 : 뒤쪽 매개변수부터 기본값을 지정해야 함
        def 함수명(매개변수, 매개변수=기본값) # ok
        def 함수명(매개변수=기본값, 매개변수) # error
'''
# 해당 함수 실행시 기본 매개변수에 전달값은 생략할 수 있음.
# 전달값이 없으면 준비된 기본값을 사용하게 됨.
# def tmain(a, b, c=0) 가능
def tmin(a=0, b=0, c=0):
    '3개의 값을 전달받아서 , 가장 작은 값을 찾아내서 리턴하는 함수'
    print(f'a : {a}, b : {b}, c :{c}')

    min_value = 0
    if a < b and a < c:
        min_value = a
    elif b < c:
        min_value = b
    else :
        min_value = c

    return min_value

def func_default_param():
    '사용할 함수가 기본값이 있는 매개변수일 때 테스트 함수'
    print('가장 작은 값 :', tmin(12, 3, 90))
    print('가장 작은 값 :', tmin(12, 3))
    print('가장 작은 값 :', tmin(12))
    print('가장 작은 값 :', tmin())

#------------------------
# 키워드 매개변수
# 함수 사용할 때 (함수 호출시) 매개변수 = 전달값의 형태로 사용하는 매개변수를 말함
# 함수명(매개변수=전달값) => 매개변수 사용 순서는 상관없음
def num_calc(a, b, c, d, e):
    return (a + b - c * d / e)

def func_keyword_param():
    '전달값을 매개변수명을 지정해서 전달하는 테스트 함수'
    result = num_calc(10, 9, 8, 7, 7)

    #매개변수 순서대로 갯수 맞춰서 값 전달해야 함
    print(f'result : {result}')
    
    # 매개변수명을 지정해서 값 전달 처리할 수 있음 : 키워드 매개변수
    result = num_calc(a=10, d=7, c=8, e=7, b=9)
    print(f'result : {result}')

#--------------------------
# 가변 매개변수 :  전달받을 매개변수의 갯수를 정하지 않은 매개변수
# 함수만들때 매개변수 앞에 *표시함.
# def 함수명(매개변수, *매개변수, 매개변수=기본값)
# 가변 매개변수는 값을 0개 ~ N개임, 값을 받을 갯수가 미정.
# 가변 매개변수의 자료형은  tuple 임
def dynamic_param(*args):
    '가변 매개변수가 받은 값을 확인하는 함수'
    print(f'args : {args}, type:{type(args)}')
    for index in range(len(args)):
        print(f'{index}번째 전달온 값 : {args[index]}')

def func_dynamic_param():
    '가변 매개변수를 가진 함수 실행 테스트용'
    dynamic_param()
    dynamic_param(10)
    dynamic_param(2, 3)
    dynamic_param(4, 5, 23, 59, 79, 11)

#----------------------
# 재귀함수(재귀적 호출 함수 : recursive call function)
# 함수안에서 자신을 실행하는 함수 (반복문)
# 주의 : 무한 루프가 되지 않도록 종료 조건 반드시 기술 할 것.
# 파이썬은 무한 루프에 빠지면 자동으로 일정 구간 반복 후에  에러 발생시킴.

def fectorial(n):
    print(n, ' * ', end=' ')
    if n == 0:
        return 1
    else:
        return n * fectorial(n-1)

if __name__ == '__main__':
    # func_param_args()
    # func_call_value()

    # func_call_address()
    # func_default_param()
    # func_keyword_param()
    # func_dynamic_param()
    print('\n10! : ', fectorial(10))


    pass

