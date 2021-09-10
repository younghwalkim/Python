from random import *

class Cabinet:
  def cabinetAdmin(userInfo, cabinetInfo):
    
    # print(userInfo)
    # print(cabinetInfo)

    cabinet = {}
    k = 0

    # 키배정
    for cabinetCode in cabinetInfo:
      
      for i in range(cabinetInfo[cabinetCode]):       

        kyeNum = cabinetCode + "_" + str(randint(1,cabinetInfo[cabinetCode]));

        while kyeNum in cabinet:
          # 중복발생
          kyeNum = cabinetCode + "_" + str(randint(1,cabinetInfo[cabinetCode]));
        else:            
          # 키 발급
          if k < len(userInfo): 
            # print("발급 " + kyeNum)
            cabinet[kyeNum] = userInfo[k]
          else:
            # 인원수 초과시 종료
            print("발급 완료")
            break;

        k = k + 1

    # print(str(cabinet) + "\n")

    return cabinet

  def cabinetWho(cabinetInfo, username):
    print(cabinetInfo)
    print(username)
        
        


    
   

