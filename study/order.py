class Order:
  def qna():
    
    cName = "kim"
    pName = "Unknown"

    while pName != cName:
      print("{0}, 커피가 준비되었습니다.".format(cName))
      pName = input("이름을 입력해주세요.")

    print("감사합니다.")      