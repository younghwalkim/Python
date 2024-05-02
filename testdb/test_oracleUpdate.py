# path : testdb\\test_oracle2.py
# 오라클 연동과 update 쿼리문 실행 테스트

# 1.
import common.dbConnectTemplate as dbtemp

# 2.
dbtemp.oracle_init()
conn = dbtemp.connect()

# 3.
# query = "update member set  userpwd = 'tp111', phone='111-1111-1111' , email='aaa@aaa.com' where userid = 'user77' "

# update 구문에 사용할 값을 외부 데이터를 이용할 경우 (키보드 입력 데이트 등)
# 주의 : 쿼리문에 적용할 외부 값은 반드시 튜플로 저장해야 함.
# 키보드로 값을 입력받아서 튜플에 저장 처리 :
tup = ()
tup = (
    input('USERPWD : '),
    input('PHONE : '),
    input('EMAIL : '),
    input('USERID : ')
)
print(tup)

# insert
# 튜플에 쿼리문을 적용할 때, 값을 1234 순으로 적용해야 함 (순서 주의)
query = "update member set userpwd = :1, phone=:2 , email=:3 where userid = :4 "

# 4.
cursor = conn.cursor()
try :
    # cursor.execute(query)
    cursor.execute(query, tup)
    conn.commit()
except :
    conn.rollback()
finally:
    cursor.close()
    dbtemp.close(conn)
