# 파이썬에서 함수 만들기 : def 키워드 사용함
# def 함수명(매개변수):
# 들여쓰기  함수의 실행 코드 작성함

def print_hi(name):
    print(f'Hi, {name}')

def test_function():
    a = 1
    b = '1'
    c = 1.1
    d = True
    e = 99999999999999999999999999999999999999999999999999999999999999999999999999999
    f = 4 + 1j
    print(type(a), type(b), type(c), type(d), type(e), type(f))

if __name__ == '__main__':
    # 함수 실행 :  함수명(전달인자)  또는   변수 = 함수명(전달인자)
    print_hi('PyCharm')  # 함수 실행 구문

    a = '안녕'
    b = '하세요'
    print(a + b)

    test_function()  # 함수 실행

    print('main 종료')

