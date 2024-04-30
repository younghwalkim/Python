# module
# 사용자 정의 모듈 사용하기

import module.mymodule as my

print('더하기 : ', my.sum(10,20))
print('빼기 : ', my.sub(10,20))
print('곱하기 : ', my.mul(10,20))
print('나누기한 몫 : ', my.div(10,20))
print('나누기한 나머지 : ', my.mod(10,20))

try:
    print('나누기한 나머지 : ', my.mod(10,0))
except Exception as msg:
    print(msg)
    pass


print('가장 큰 값 : ', my.max())
print('가장 큰 값 : ', my.max(10))
print('가장 큰 값 : ', my.max(10, 20, 30, 40, 50))

print('가장 큰 값 : ', my.min())
print('가장 큰 값 : ', my.min(10))
print('가장 큰 값 : ', my.min(10, 20, 30, 40, 50))

print('글자 갯수 : ', my.strlen())
print('글자 갯수 : ', my.strlen('module test'))

print('원주율 : ',my.pi)
print('카운트 : ',my.count)



