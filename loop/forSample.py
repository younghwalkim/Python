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

def sim():

    # 간결 문장
    list = []
    for i in range(5):
        list.append(i)
    print(list)

    print([i for i in range(5)])