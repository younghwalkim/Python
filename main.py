from study import *


# 케비넷관리
userInfo = ["유재석","하하","김태호","김종국","조세호"]
cabinetInfo = {"A":2,"B":8}

cabinetResult = Cabinet.cabinetAdmin(userInfo, cabinetInfo)

Cabinet.cabinetWho(cabinetResult,"김태호")

Cabinet.cabinetUnused(cabinetResult, cabinetInfo)



# 로또번호
# Lotto.lotto(5)