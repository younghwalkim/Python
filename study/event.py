from random import *

class Event:
  def gift():
    print("1명 치킨, 3명 커피, 20명 참여, 랜덤 추첨, 중복불가, shuffle, sample 활용 \n")

    # 방법 1. 참여자 명단 만들기
    # userID = []
    # for i in range(20):
    #  userID.append(i+1)

    # 방법 2. 참여자 명단 만들기
    userID = range(1,21)
    # print(type(userID))
    # print(str(userID) + " \n")

    userID = list(userID)
    # print(type(userID))
    # print(str(userID) + " \n")

    # 명단 섞기
    shuffle(userID)
    # print(str(userID) + " \n")

    # 4명 추첨
    winners = sample(userID,4)
    # print(str(winners) + " \n")

    # 치킨 1명, 커피 3명 발표
    print(" -- 당첨자 발표 -- ")
    print("치킨 당첨자 : {0}".format(winners[0]))
    print("커피 당첨자 : {0}".format(winners[1:]))
    print(" -- 축하합니다. -- ")
    