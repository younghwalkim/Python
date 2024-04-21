class File:
  def write():
    score_file = open("readWriteFile.txt","w",encoding="utf8")
    
    print("11111", file=score_file)
    print("22222", file=score_file)
    
    score_file.write("33333 \n")
    score_file.write("44444 \n")

    score_file.close()

  def read(self):
    score_file = open("1.txt","r",encoding="utf8")
    print(score_file.read())
    score_file.close()    

  def readline(self):
    score_file = open("1.txt","r",encoding="utf8")
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")        
    score_file.close()

  def readline_while(self):
    score_file = open("1.txt","r",encoding="utf8")
    while True:
      line = score_file.readline()
      if not line:
        break
      print(line, end="")

    print(type(line))

    score_file.close() 

  def readline_list(self):
    score_file = open("1.txt","r",encoding="utf8")    
    lines = score_file.readlines() # list 형대로 저장
    
    for line in lines:
        print(line, end="")
    
    print(type(lines))

    score_file.close()     