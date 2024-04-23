# 파이썬 제어문 실행용 시작 스크립트

# 다른 파일에 있는 함수를 사용하려면 import 선언해야 함.
# 파일이 제공하는 함수 사용시, 디렉토리명.파일명. 함수명(...
# 모듈명이 길거나 복잡할 경우 줄임말 지정하고 사용 가능함.
# import 모듈명 as 줄임말

import test_bool.operator_sample as to
import chapter.ifSample as cif
import mission.ifMission1 as com2

# 프로그램을 시작하는 구문임
if __name__ == '__main__':
    # 임포트한 파일에서 제공하는 함수 사용.
    # 모듈명.함수명() 또는 줄임말.함수명()
    # to.func_bool1()
    # to.func_bool2()
    # to.func_compare()
    # to.func_logical()

    # 제어문 (조건문, 반복문, 분기문)
    # cif.test_if1()
    # cif.test_if2()
    # cif.test_even_add()
    # cif.test_range()
    # cif.test_in()
    # cif.checkPayment1()
    # cif.checkPayment2()
    # cif.multi_if()
    # cif.shortCondition1()
    # cif.shortCondition2()

    #
    com2.practice1()
    com2.practice2()
    com2.practice3()
'''
    a = 2
    if (a==1) :
        print(1)
    else:
        print(2)

    a = 1

    if (a > 0):
        msg = 'a는 양수입니다.'
    else:
        msg = 'a는 음수입니다.'
    print(msg)

    if(a==0):
        msg2 = 'a는 0입니다.'
    else:
        msg2 = 'a는 0이 아닙니다.'
    print(msg2)
    
'''