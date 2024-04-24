# path : loop\\whileMission.py
# module : loop.whileMission
# while 문 실습문제
'''  prompt 변수를 while 문으로 반복해서 출력하면서, 입력되는 번호에 따라
sungjuk_list 의 아이템을 추가하거나 삭제하거나 출력되게 작성하시오.
1 입력 : 리스트에 아이템 값들을 입력받아 추가함
  번호 : 24 (sno : int)
  이름 : 이순신 (sname : str)
  점수 : 100 (score : int)
  ==> 리스트에 추가 처리함    ==> 새로운 학생정보가 추가되었습니다.  출력함
2 입력 : 리스트의 인덱스 위치의 아이템 제거함
  현재 저장된 아이템의 갯수는 3개 입니다.  출력함
  제거할 아이템의 순번 : 3    ==> 입력받은 인덱스 위치의 아이템 제거함
  ==> 3번 위치의 아이템이 제거되었습니다.  출력함   ==> 현재 저장된 아이템의 갯수는 2개 입니다.  출력함
  ==> 잘못된 인덱스 입력시 :   '순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.' 출력함
3 입력 : 저장된 리스트 정보 아이템별로 출력함
  0 : [12, '홍길동', 98]
  1 : [15, '김유신', 87]
  2 : .......
4 입력 : while 반복 종료함
  성적관리 프로그램이 종료되었습니다.  출력함
'''
def sungjuk_process():
    # sungjuk_list = []
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    prompt = '''
            *** 원하는 메뉴 번호를 선택하세요. ***
            1. 추가
            2. 삭제
            3. 출력
            4. 끝내기
        '''

    while True:
        print(prompt)
        no = int(input('번호 입력 : '))

        if no == 1:
            # 기존 리스트에 추가하는 코드 작성
            sno = int(input('번호 : '))
            sname = input('이름 : ')
            score = int(input('점수 : '))

            sungjuk_list.append([sno, sname, score])
            print('새로운 학생정보가 추가되었습니다.')

        elif no == 2:
            # 제거할 인덱스를 입력받아서 리스트에서 제거하는 코드 작성
            print('현재 저장된 아이템의 갯수는 %d 개입니다.' % len(sungjuk_list))
            idx = int(input('제거할 아이템의 순번 : '))

            if (idx >= 0 and idx < len(sungjuk_list)):
                sungjuk_list.pop(idx)
                print(idx, '위치의 아이템이 제거되었습니다.')
                print('현재 남은 아이템의 갯수는 %d 개입니다.' % len(sungjuk_list))
            else:
                print(f'{idx} 순번을 잘못 입력하였습니다. 다시 입력하세요.')

        elif no == 3:
            # 리스트 안의 각 아이템 정보를 출력하는 코드 작성
            for idx in range(len(sungjuk_list)):
                print(f'{idx} : {sungjuk_list[idx]}')

        elif no == 4:
            break
    # while end

    print('========== 성적 처리 프로그램이 종료되었습니다. ==========')
# def  sungjuk_process() end --------------------------


# 함수 실행 ---------------------------
if __name__ == '__main__':
    sungjuk_process()
