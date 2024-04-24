# path : loop\\loopMission.py
# module : loop.loopMission

# 리스트 안의 튜플 아이템의 값들에 대해, 둘 중의 큰값과 작은값을 분류해서 출력 처리

# 방법 1 : 조건식 직접 작성
def practice1():
    nlist = [(12, 45),( 90, 32), (56, 19)]
    # for 문 in if 문 사용
    for num1, num2 in nlist:
        if num1 > num2 :
            print(f'{num1} 과 {num2} 중 큰수는 {num1} 이다.')
        else :
            print(f'{num1} 과 {num2} 중 큰수는 {num2} 이다.')

# 방법 2 : 내장함수 이용 - max
def practice2():
    nlist = [(12, 45),( 90, 32), (56, 19)]
    for num1, num2 in nlist:
        result = max(num1, num2)
        print(f'{num1} 과 {num2} 중 큰수는 {result} 이다.')

# 활용 실습 : 조건식 직접 작성
# 리스트 안의 군집아이템들이 가진 값들 중 각각 가장 큰 값을 골라 내서, 별도의 리스트에 저장 처리하고 출력
def practice3():
    nlist = [(3, 1, 20 ), (22, 41, 10, 73), {12, 32, 45, 3, 9}]
    max_list = []

    for item in nlist:
        print(item, type(item))
        item_max = 0

        for idx in item:
            print(idx, type(idx))

        # max_list.append(item_value)
    print(max_list)

# 내장함수 max(Iterable) 사용
def practice4():
    None

''' while 문 실습문제
아래의 작성된 for문을 while문으로 변경하시오.
sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

for student in sungjuk_list:
    if(student[2] >= 60):
        print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]))
    else:
        print('{}번 {} 학생은 불합격입니다.'.format(student[0], student[1]))
'''
# 1. while 문으로 변경
def practice_while():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]



# 2. for 문 안에 continue 를 사용해서 합격자 정보만 출력되게 처리
def practice_continue():
    None

# 3. print() 안에 간단 if 문 사용해서 출력 처리
def practice_short_if():
    None

if __name__ == '__main__':
    # practice1()
    # practice2()
    practice3()