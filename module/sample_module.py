
# path : module\\sample_module.py
# module : module.sample_module
# 파이썬에서 모듈 만들어서 사용.

# 모듈(module) : 파이썬 소스 파일이다. (파일명.py)
# 파일명이 모듈명이 됨.

# 모듈용 소스 파일에는 함수와 전역변수가 저장되면 됨.
# 모듈이 제공하는 함수와 전역변수를 사용하려면, import 모듈명으로 선언한 다음에
# 모듈명.함수명), 모듈명.변수명으로 사용하면 됨.

# import keyword
# keyword.py 파일을 의미함.

# print(keyword.kwlist)  # 모든 키워드 출력

# 모듈은 다른 파이썬 파일에서 사용할 수 있다록 함수(기능)와 변수(값)들을 따로 저장해서 제공하는 목적의 소스파일이다.

# 모듈 import 시에 모듈명에 대한 줄임말을 같이 선언할 수도 있음.
# import 모듈명 as 줄임말.
# import keyword as k
# print(k.kwlist)
# print(k.__file__)     # 해당 모듈(파일)의 위치가 출력됨.
# help('modules')     # 현재 설치되어 있는 모듈 확인

# 모듈 설명 참조
# help('random')

#----------------------
# 파이썬이 제공하는 표준 모듈
# import os
# print(os.getcwd())

# import time
# print(time.localtime()) # 현재 날짜와 시간 정보 출력
# time.sleep(1)   # 1초 멈춤
# print(time.localtime())

# import random
# print(random.random())
# print(random.randint(1,5)) # 1 <=  random <= 5
# print(random.randrange(1,10, 2))

# import math
# print(math.pi)
# print(math.factorial(5))

import calendar
calendar.prmonth(2024,5)
print(calendar.prmonth(2024,5))


# __name__ 현재사용되고 있는  모듈이름 확인
print(__name__) #main 파일명 출력됨
# 프로그램을 실행하면 기본 파일은 main 모듈(파일) 이 됨, 즉, main만 실행할수 있다는 의미임.