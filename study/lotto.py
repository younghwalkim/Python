from random import *

class Lotto:
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