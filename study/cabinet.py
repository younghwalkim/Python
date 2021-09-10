from random import *

class Cabinet:
  def cabinetAdmin(userInfo, cabinetInfo):
    
    # print(userInfo)
    # print(cabinetInfo)

    cabinet = {}
    count = 1

    for cabinetCode in cabinetInfo:
      
      for i in range(cabinetInfo[cabinetCode]):       

        kyeNum = cabinetCode + "_" + str(randint(1,cabinetInfo[cabinetCode]));
        
        # 중복제거
        if kyeNum in cabinet:
          kyeNum = cabinetCode + "_" + str(randint(1,cabinetInfo[cabinetCode]));
          print("중복")

          while kyeNum not in cabinet:
             cabinet[kyeNum] = "."
        else: 
          cabinet[kyeNum] = "."

        print(kyeNum)
        print(count)
        count = count + 1
        


    
    print(cabinet)

