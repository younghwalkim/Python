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
            # 인원 초과시 발급 종료
            # print("발급 완료"  + kyeNum + " \n")
            break;

        k = k + 1
    print("발급 완료")
    print(str(cabinet) + "\n")

    return cabinet

  def cabinetWho(cabinetInfo, username):
    # print(cabinetInfo)
    # print(username)

    for i in cabinetInfo: 
      if cabinetInfo[i] == username:
        print(username + " 님의 캐비넷 번호는 "+ i + " 입니다. \n")

  def cabinetUnused(cabinetResult, cabinetInfo):   
    # print(cabinetInfo) 

    UnusedKey = []

    for cabinetCode in cabinetInfo:      
      for i in range(cabinetInfo[cabinetCode]):   
        kyeNum = cabinetCode + "_" + str(i+1);
        
        if kyeNum not in cabinetResult:
          UnusedKey.append(kyeNum)
    
    print("미사용 캐비넷 번호" + str(UnusedKey) + " 입니다. \n")


    
   

