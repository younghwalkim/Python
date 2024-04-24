# loop.forSample
import collections.abc


def test_for1():
    # 리스트
    print('##리스트 예##')
    for i in [1,2,3]:
        print(f'{i}')

    # 튜플
    print('##튜플 예##')
    for i in (11, 22, 33):
        print(f'{i}는  짝수다' if i % 2 == 0 else f'{i}홀수다')

    # set
    print('##Set 예##')
    for i in {1, 2, 3}:
        print(f'{i} 의 제곱은 {i**2} 이다 ' )

    # str
    print('##str 예##')
    for i in "hello":
        print(i)

def test_for2():

    list = ['a', 9, [1, 2, 3], ('a', 'b')]
    for i in list:
        print(i)

    # index 활용
    for i in range(len(list)):
        print(list[i])

    # 1~100 정수 합계
    list = []
    sum = 0
    for i in range(101):
        list.append(i)
        if i == 100 :
            print(list[i], end=' = ')
        else :
            print(list[i], end=' + ')
        sum = sum + list[i]

    print(sum)

def test_Iterable():
    nlist = [1,2,3,4]
    print( isinstance(nlist, collections.abc.Iterable))


def test_range():
    #print(range(10))

    lst = list(range(10))
    print(lst)

    # 간결 문장

def test_indexing():
    list1 = ['apple', 90, [1,2,3], ['a','b','c']]
    for item in list1:
        print(item)

    for i in range(len(list1)):
        print(list1[i])

    # print( i for i in range(len(list1)) )

# 입력 단수 출력
def print_gugudan():
    num = input("출력할 단 수를 입력해주세요.")

    for i in range(1, 10):
        print("{} X {} = {}".format(num, i, int(num) * i))

# 2단~9단
def doubleFor():
    for i in range(2, 10):
        for j in range(1, 10):
            print("{} X {} = {}".format(i, j, int(i) * j))
        print("--------")

    print([i * j for i in range(2, 10) for j in range(1, 10)
           if i != 4])

# 리스트 | 튜틀 | 셋 안의 리스트 | 튜플 | 셋이 저장된 경우
# 이중 for 문 사용 필요.

# 예1) 리스트 안의 아이템 안의 값의 갯수가 동일한 경우에는 단순 for문 적용 가능.
def list_in_list1():
    fruit_list = [['apple', 10, 800], ['banana', 3, 2500], ['orange',15, 500]]

    for fname, famount, fprice in fruit_list:
        print(f'{fname} 의 단가는 {fprice} 원이고, 구매수량은 {famount}개, 구매가격은 {fprice * famount}원')

# 예2) 리스트 안의 아이템 안의 값의 갯수가 다른 경우에는 이중 for문 적용
def list_in_list2():
    nlist = [['a', 'bb', 'ccb'],[10,20],[1, 2, 3, 33, 89]]

    for item in nlist:
        print(item)
        for i in item:
            print(i)
        print('-----')

def list_in_list3():
    nlist = [['a', 'bb', 'ccb'],[10,20],[1, 2, 3, 33, 89]]

    for index in range(len(nlist)):
        print(nlist[index])
        for inindex in range(len(nlist[index])):
            print(nlist[index][inindex])
        print('-----')


