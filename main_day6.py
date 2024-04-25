# Random test

import  random as rd

def test_random():
    # 0.0 <= 랜덤값 < 1.0 범위의 실수형 값 발생
    print('랜덤값 출력 : ', rd.random())

    # 범위 지정 : start <= 랜덤값 < stop 범위의  정수형 값 발생
    print('1~10 랜덤값 확인 : ', rd.randrange(1,11))

# 1부터 45

def lotto_set():
    # 셋 선언 (중복 불가)
    numbers = set()

    # 담기
    while len(numbers) < 6 :
        numbers.add(rd.randrange(1,46))

    lotto_nums = list(numbers)
    lotto_nums.sort(reverse=False)

    print(lotto_nums)


def lotto(cnt):

    # 시도횟수
    for k in range(cnt):

        # 배열정의
        arrnum = []

        # 6자리
        while len(arrnum) < 6:

            # 1 ~ 45 숫자 추출
            num = rd.randint(1, 45)

            # 추출된 숫자 중 중복값 제거
            if num not in arrnum:
                arrnum.append(num)

        # 정렬
        arrnum.sort()

        # 출력
        print(f'{k+1}개 출력 : {arrnum}')

# 프로그램을 시작하는 구문임
if __name__ == '__main__':
    # test_random()

    lotto_set()

    # num = int(input('몇 개 출력하시겠나요? '))
    # lotto(num)