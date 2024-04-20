# test_dict\dict_sample.py
# 모듈로 표현 : test_dict.dict_sample
# 모듈(module) : 함수들을 따로 모아서 저장해 놓은 소스 파일들의 묶음

# 사전(dict) 자료형
# 자바의 Map 과 같은 구조로 key 와 value 를 쌍으로 저장하는 집합자료형임
# dict 에서 key 는 변경되지 않는 값이어야 함 (키는 지정하면 변경할 수 없음) => 키에 튜플을 사용할 수 있음
# dict 에 저장하는 value 는 모든 자료형 데이터 가능함
# json, xml 로 변환할 때 많이 사용됨

# dict 정의방법 1 : dict() 함수 사용
def test1():
    dict1 = dict()
    print(dict1, type(dict1))

# dict 정의방법 2 : {} 중괄호 사용
def test2():
    dict1 = {}
    print(dict1, type(dict1))

# list 나 tuple 처럼 인덱스를 사용할 수 없음 : 인덱스 없음
# 키(key)를 이용해서 값 변경, 조회, 추가할 수 있음 : 사전변수[키]
# 키는 변경할 수 없음 , 키에 튜플 사용할 수 있음
# 값은 자료형에 제한없음

# dict 에 값 저장 방식 : {키:값} 쌍으로 저장함
def test3():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    print(dict1, type(dict1))

def test4():
    dict1 = {1: 'python', 'a': [1, 2, 3], (1, 2): 345}
    print(dict1, type(dict1))

    # 값 변경 : 사전변수[키] = 바꿀값
    # 저장되어 있는 키만 사용해야 함
    dict1['a'] = 77
    print(dict1, type(dict1))

    # 아이템 추가 : 사전변수[키] = 값
    # 저장되어 있지 않은 키를 사용함
    dict1[3] = [11, 2, 33]
    print(dict1, type(dict1))

    # 값 조회 : 사전변수[키]
    # 주의 : 없는 키로 조회하면 KeyError 발생함
    # print(dict1['c'])    # error
    print(dict1['a'])

# dict 내장함수 활용
def test5():
    dict1 = {
        'a': 10,
        'b': 25,
        'c': 77
    }
    print(dict1, type(dict1))

    # 키에 대한 리스트 만들기 : keys() 함수
    print('dict1 의 키 목록 : ', dict1.keys())

    # 값에 대한 리스트 만들기 : values() 함수
    print('dict1 의 값 목록 : ', dict1.values())

    # (키, 값) 을 item 이라고 함, 아이템을 리스트 만들기 : items() 함수
    print('dict1 의 아이템 목록 : ', dict1.items())

# 사전과 사전을 합치기 : update() 함수 사용
# 사전1.update(사전2)  => 사전1을 변경함
# 사전1과 사전2에 동일한 키가 있을 경우에는, 사전1의 해당 키의 값이 변경됨
def test6():
    dict1 = {'name': '갤럭시', 'price': 1200000, 'tax': 0.1}
    dict2 = {'content': '최신 모델입니다.', 'price': 880000}
    print('dict1 : ', dict1)
    print('dict2 : ', dict2)

    dict1.update(dict2)
    print('dict1 : ', dict1)

# dict 내장함수 2
def test7():
    dict1 = {'name': '갤럭시', 'price': 1200000, 'tax': 0.1}
    print('dict1 : ', dict1)

    # pop(key) 함수 : 해당 키에 대한 아이템을 꺼내면서 제거함
    tax = dict1.pop('tax')
    print('dict1 : ', dict1)
    print('tax: ', tax)

    # clear() 함수 : 딕셔너리 안을 비움 (저장 아이템 전체 삭제)
    dict1.clear()
    print('dict1 : ', dict1)

    dict2 = {'content': '최신 모델입니다.', 'price': 880000}
    print('dict2 : ', dict2, id(dict2))    # id(변수) : 할당 위치에 대한 id 값 확인 (자바의 hashCode 와 같음)

    # copy() 함수 : 딕셔너리 객체를 새로 만들고 아이템들을 복사함 (deep copy)
    dict3 = dict2.copy()
    print('dict3 : ', dict3, id(dict3))

    dd = dict2          # 주소복사  : 얕은 복사 (shallow copy)
    print('dd: ', dd, id(dd))

# dict 안에 키 또는 값이 존재하는지 확인 : in 사용
def test8():
    dict1 = {'name': '갤럭시', 'price': 1200000, 'tax': 0.1}
    print('dict1 : ', dict1)

    # 키 존재 여부 : 키 in 사전변수
    print('name 키가 존재하느냐? ', 'name' in dict1)   # True
    print('content 키가 존재하느냐? ', 'content' in dict1)  #  False

    # 값 존재 여부 : 값 in 사전변수.values()
    print('0.1 값이 존재하느냐? ', 0.1 in dict1.values())  # True
    print('880000 값이 존재하느냐? ', 880000 in dict1.values())  # False

    # 키로 값 조회 : 사전변수[키] == get(key)
    print('name : ', dict1['name'], dict1.get('name'))

    # 아이템 제거시 pop(key)  => 없는 키 사용하면 에러남
    dict1.pop('tax')
    # print('tax : ', dict1['tax'])   # error
    print('tax : ', dict1.get('tax'))   # None 리턴

    # del 사전변수[키]
    del dict1['name']
    print('dict1 : ', dict1)



