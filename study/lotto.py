from random import *

class Lotto:
  def taxi():

    cnt = 0

    for i in range(1,51): # 1~50 승객수
      mtime = randint(5,51) # 5분~50분 소요시간
      
      if mtime in range(5,16): # 5분~15분 이내 승객, 증가처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, mtime))
        cnt = cnt + 1
      else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, mtime))

    print("")
    print("총 탑승 승객 : {0} 분".format(cnt))

  def lotto(cnt):

    # 시도횟수
    for k in range(cnt):

      # 배열정의
      arrnum = []

      # 6자리 
      while len(arrnum) < 6 :
        
        # 1 ~ 45 숫자 추출
        num = randint(1,45)

        # 추출된 숫자 중 중복값 제거
        if num not in arrnum:
          arrnum.append(num)

      # 정렬
      arrnum.sort()

      # 출력
      print(arrnum)