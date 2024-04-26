# path : function\\func_lambda.py
# module : function.func_lambda
# 파이썬에서 람다함수 만들어 사용하기
'''
리스트 내포(list in for), 간단 조건문처럼 여러줄로 된 코드를
간결하게 표현할 수 있는 새로운 함수 정의 방법

작성과 사용법 :
참조변수 = lambda 매개변수, 배개변수 : 처리구문
case1) 참조변수(전달값, 전달값)
case2) (lambda 매개변수, 매개변수: 처리구문)(전달값, 전달값)
'''

# 일반 함수
def add(x,y):
    return x + y

# 람다 함수
add2 = lambda x,y : x+y

if __name__ == '__main__':
    # 일반함수
    print('일반함수 : ', add(5,6))

    # 람다함수
    print('람다함수 : ', add2(5,6))

    # 람다함수는 주로 작성과 실행을 함께 처리하는 방식으로 사용됨.
    print('더하기 결과 : ', (lambda  x,y : x+y)(5,6))

    # 람다함수의 매개변수에도 기본, 키워드, 가변 매개변수 적용 가능.
    print('(기본) 더하기 결과 : ', (lambda x, y=6: x + y)(5))
    print('(키워드) 더하기 결과 : ', (lambda x, y: x + y)(x=5, y=6))
    print('(가변) 적용 결과 : ', (lambda x, *y: x *y)(5, 1,2,3))

    # 람다함수 안에 간단 조건문 사용할 수 있음
    print((lambda  x, y : x if x % 2 == 0 else y)(5, 6))
