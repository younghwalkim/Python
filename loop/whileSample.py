# loop.whileSamply
# 반복횟수가 정해지지 않은 경우는 while 문 사용

def test_while():
    num = 5
    while num > 0 :
        print(num)
        num -= 1

def print_unicode1():
    ch = input('문자하나 입력 [단, 0이 입력되면 종료됨] : ')

    while ch !='0':
        print(f'{ch} is unicode {ord(ch)}')
        ch = input('문자하나 입력 [단, 0이 입력되면 종료됨] : ')

def print_unicode2():
    while True:
        ch = input('문자하나 입력 [단, 0이 입력되면 종료됨] : ')
        if ch == '0':
            break
        print(f'{ch} is unicode {ord(ch)}')

def display_menu():
    prompt = '''
*** 원하는 메뉴 번호를 입력하세요. ***
    1. 추가
    2. 삭제
    3. 출력
    4. 끝내기
    '''
    while True:
        print(prompt)
        no = int(input('번호 입력 : '))

        if no == 4 :
            break

    print('--- 종료 ---')



# 실행파일 설정
if __name__ == '__main__':
    display_menu()
