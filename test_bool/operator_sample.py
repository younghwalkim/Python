# test_bool\\operator_samply.py or test_bool/operator.py
# 모듈로 표현 : test_bool.operator.py

# bool 자료형을 확인하는 함수
def func_bool1():
    flag = True
    print('flag : ', flag, type(flag))

    flag = False
    print('flag : ', flag, type(flag))

# bool() 함수 사용 : 값의 논리상태를 확일할때 사용
def func_bool2():
    print('result1 : ', bool('abcd'))
    print('result2 : ', bool(''))

    #  값이 저장되어 있는지, 비어 있는지 확인하는 용도로 사용할 수 있음
    print('result3 : ', bool({'a':1, 'b':2}))
    print('result4 : ', bool({}))

    print('result5 : ', bool([1,2,3,4]))
    print('result6 : ', bool([]))

    print('result7 : ', bool((1,2,3,4)))
    print('result8 : ', bool(()))

    print('result9 : ', bool(1))
    print('result9 : ', bool(0))

# 비교(관계) 연산자
# > (초과), < (미만), ==, !=, >=(이상), <= (이하)
# 이항연산자 : 값1 연산자 값2
def func_compare():
    print('1 = 1 : ', 1 == 1)
    print('1 = 2 : ', 1 == 2)

    print('1 > 0 : ', 1 > 0)
    print('1 < 2 : ', 1 < 2)

    print('1 >= 1 : ', 1 >= 1)
    print('1 != 0 : ', 1 != 0)

# 논리연산자 : 논리값(True, False) 를 계산에 사용하는 연산자
# and, or, not
def func_logical():
    a = 1
    b = 2
    print( a > 0  and b > 1)
    print(a == 0 or b != 1)
    
    # and 연산자의 특징
    # 앞 and 뒤 : 앞이 false 이면 뒤를 실행 안 함
    # 앞이 True 이면 뒤를 실행함.
    # 이 성질을 이용하는 짧은 조건문이 있음 (모든 스크립트에서 사용 가능함)
    print('a and b : ', 'a' and 'b')
    print('   and b : ', '' and 'b')

    # or 연산자의 특징
    # 앞 or 뒤 : 앞이 false 이면 뒤를 실행함.
    # 앞이 True 이면 뒤를 실행 안함.
    print ('a or b : ', 'a' or 'b')