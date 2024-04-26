# path : function\\func_lambda2.py
# module : function.func_lambda2
# 람다함수를 이용하는 파이썬 내장함수 사용 테스트

# map 내장함수 :
# 맴객체변수 = map(실행할 함수명, 시퀀스 캑체)
# 시퀀스(Sequence) 객체 : 값을 순차적으로 저장하는 객체. 리스트나 튜플이 해당됨.
# 시퀀스 객체의 각 요소값을 하나씩 꺼내서 함수로 보내고,
# 처리결과를 린턴받아서 맴객체에 저장하는 함수

def func(x):
    return  x * x

def test_map():
    list1 = [1, 2, 3, 4, 5]
    m = map(func, list1)
    print(m, type(m))   # 맴참조변수 출력 : 참조객체 타입과 16진수 주소(id)가 출력됨.
    print(list(m))

    # 하수명 대신에 람다함수로 작성을 바꾼다면
    m = map((lambda x : x*x), list1)
    print(list(m))
    
    # 람다는 코드를 간결하게 표현하는게 목적임
    print(list(map((lambda x : x*x), [1, 2, 3, 4, 5])))

#----------------------
# filter 내장함수
# 필터결과객체 = fliter(실행할 함수명, 시퀀스 객체)
# 시퀀스 객체의 각 요소의 값에 대해 함수 처리 결과가 참(True) 인 요소만 골라서 저장하는 함수

def func1(x):
    return x > 2

def test_filter():
    nlist = [1, -2, 4, 7]
    f = filter(func1, nlist)
    print(f, type(f))
    print(list(f))

    # 람다 적용
    print(list(filter((lambda x : x > 2), [1, -2, 4, 7])))


if __name__ == '__main__':
    # test_map()
    test_filter()