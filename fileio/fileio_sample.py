# fileio.fileio_smaple
# 파일 입출력 처리
# open() --> write() or read() --> close()
'''
파일변수 = open('디렉토리명\\파일명.확장자', '열기모드')
열기모드
    w(wt) : 새로쓰기, 대상파일 없으면, 새로 만듦, 있으면 내용 지우고 새로 쓰기.
    x(xt) : 새로쓰기, 없으면, 새로 만듦, 있으면 에러 발생
    r(rt) : 읽기
    a(at) : append - 추가 쓰기, 없으면, 새로 만듦, 있으면 파일내용에 추가
'''

import os

# 파일 새로 만들고 값 기록.
def test_fwrite1():

    # 파일 open 시 인코딩 문자셋 지정하면, 문자 깨짐 해결  - utf-8
    # f = open('testa.txt', 'w')   # 기본경로는 현재 폴더에 저장됨.
    f = open('testa.txt', 'w', encoding='utf-8')

    f.write('12345')
    f.write('abcde')
    f.write('가나다라마')  # 텍스트 파일 인코딩이 'ms949' 문자셋임,
    f.write('＠＃★')        # 한글과 기호는 깨짐

    f.close()

    # os 모듈을 활용하면 현재 작업중인 디렉토리 경로 확인.
    print(os.getcwd())

# 원하는 디렉토리에 파일을 만들려면
# open() 함수 첫번째 인자에 전체경로명과 파일명을 함께 입력하면 됨.
# 경로(path)는 백슬러시(\)  이스케이프 문자를 반드리 2개로 표시해야 함.
def test_fwrite2():
    # x 모드 : 대상파일 존재시 에러 발생 (덮어쓰기 방지)
    f = open('D:\\2. source_python\\fileio\\testb.txt', 'x', encoding='utf-8')

    f.write('12345\n')
    f.write('abcde\n')
    f.write('가나다라마\n')
    f.write('＠＃★\n')

    f.close()

# a 모드 :  append (추가)
def test_fwrite3():
    f = open('testc.txt', 'a', encoding='utf-8')

    f.write('12345\n')
    f.write('abcde\n')
    f.write('가나다라마\n')
    f.write('＠＃★\n')

    f.close()

# 파이썬에서 파일이나 데렉토리 다루기
# os 모듈이 제공하는 함수 사용
def test_osmodule():

    # 사용중인 컴퓨터의 사용자 계정
    print(os.getlogin())
    #  현재 작업 디렉토리
    print(os.getcwd())

    # 디렉토리 만들기 : os.mkdir('만들  디렉토리 경로와 디렉토리명')
    system_user = os.getlogin()
    work_dir = 'C:\\users\\'+ system_user + '\\python'
    os.mkdir(work_dir)
    
    # 현재 작업토리 변경하기
    os.chdir(work_dir)
    print(os.getcwd())

# 리스트, 투플, 셋, 딕셔너리 등에 저장한 데이터들을 파일에 저장
# writelines() 함수 사용
def test_writelines():
    tp = ('a', 'b', 'c')
    ls = ['r', 'e', 'd']

    f = open('list.txt', 'w')

    f.writelines(tp)
    f.write('\n')
    f.writelines(ls)
    f.write('\n')

    # 각 아이템별로 한 줄씩 기록을 원하면, write() 반복 실행하면 됨.
    for item in ls:
        f.write(str(item)) # 문자가 아닌 아이템은 str() 사용함
        f.write('\n')
    f.close()

# r(rt, read text) : 읽기 전용
# 주의 : 대상파일 없으면 에러남
# read() : 파일 전체 내용을 한번에 읽음
# readline() : 파일 안의 내용을 한줄씩 읽음,
#                   마지막 라인을 읽은 후, 읽을 내용이 없으면 None 리턴함
# readlines() : 파일의 내용을 줄 단위(아이템)로 읽어서 리스트로 변환함.

def test_fread1():
    print(os.getcwd())

    # f = open('sample.txt', 'r', encoding='utf-8')
    f = open('testb.txt', 'r', encoding='utf-8')

    # 파일 전체 읽기
    # print(f.read())

    # 파일 내용을 한줄씩 읽기. readline
    while True:
        line = f.readline()
        if not line: # line 변수의 값이 없다면, == None
            break
        print(line, end='')

    f.close()

def test_fread2():
    f = open('testb.txt', 'r', encoding='utf-8')

    flist = f.readlines()
    print(flist)

    f.close()

if __name__ == '__main__':
    # test_fwrite1()
    # test_fwrite2()
    # test_fwrite3()
    # test_osmodule()
    # test_writelines()
    # test_fread1()
    test_fread2()

