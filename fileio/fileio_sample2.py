import os
import pickle

# 파이썬의 '기본 파일' 입출력은 '텍스트 파일' 입출력임
# 텍스트가 아닌 자료형의 파일을 다룰 때는  pickle 모듈 활용.
# 바이너리(이진데이터:binary) 형식의 파일로 저장해야 함.
# 열기모드 : wb, rb, ab 로 표기해야 함.

def test_binary_fio1():
    data = {1: 'python', 2: 'you need'}

    f = open('btest.dat', 'wb')
    pickle.dump(data, f)  # 파일에 딕셔너리 객체가 이진 데이터로 기록됨.
    f.close()

def test_binary_fio2():
    f = open('btest.dat', 'rb')
    read_data = pickle.loads(f)
    f.close()

    print(read_data)
    print(type(read_data))


# 표준 입출력을 파일로 대상을 변경할 수 있음
# 표준입력
# 표준출력
import sys
def change_stdinout():
    stdout = sys.stdout

    f = open('text.txt', 'w', encodings='utf-8')
    sys.stdout = f
    print('표준 출력을 바꾸어 파일에 내용이 기록됨.')
    f.close()

    sys.stdout = stdout
    print('콘솔에 출력확인')


# os 모듈의 함수 사용
# 디렉토리 만들기 : mkdir(), 디렉토리 변경하기 : chdir()
# 사용자 계정 조회  : getlogin(), 현재 작업디렉토리 조회 : getpwd()
# 시스템 환경변수, 디렉토리, 파일 다룰 때 주로 이용함.
def test_os():
    # listdir() :해당 디렉토리 안의 파일과 하위 디렉토리 목록 조회
    print(os.listdir('.'))
    print(os.listdir('../'))

    # rename(): 디렉토리나 파일의 이름 바꾸기함.
    # os.rename('testa.txt', 'sample.txt')

    # path.exists() : 파일이나 디렉토리의 존재여부 확인
    print(os.path.exists('sample.txt'))
    print(os.path.exists('sample1.txt'))

    # path.abspath() :  파일이나 디렉토리의 절대경로 조회
    print(os.path.abspath('sample.txt'))

    f = open(os.path.abspath('sample.txt'), 'a', encoding='utf-8')
    f.write(os.path.abspath('sample.txt'))

    f.close()

    # path.basename(), dirname(), split() : 파일명, 경로명, 두개 분리
    
    # path.splitdrive(), splittext() : 경로에서 드라이브명만, 확장자만 추출


if __name__ == '__main__':
    # test_binary_fio1()
    # test_binary_fio2()
    # change_stdinout()
    test_os()
