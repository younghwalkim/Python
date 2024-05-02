# path : testdb\\test_oracleDelete.py
# 오라클 연동과 delete 쿼리문 실행 테스트

# 1.
import cx_Oracle
import os
import common.dbConnectTemplate as dbtemp

# 2.
dbtemp.oracle_init()
conn = dbtemp.connect()

# 3.
# query = "delete from member where userid = 'user77'"

# delete 구문에 사용할 값을 외부 데이터를 이용할 경우 (키보드 입력 데이터 등)
# 주의 : 쿼리문에 적용할 외부 값은 반드시 튜플로 저장해야 함
# 키보드로 값을 입력받아서 튜플에 저장 처리 :
userid = input('삭제할 회원 아이디 : ')

tp_value = (userid, ) # 튜플로 저장 : 저장할 값이 한개이면 반드시 , 표기함

# 튜플을 쿼리문에 적용할 때, 값을 1234 순으로 적용해야 함 (순서 주의)
query = "delete from member where userid = :1"

# 4.
cursor = conn.cursor()

try:
    # cursor.execute(query)
    cursor.execute(query, tp_value)
    conn.commit()
except:
    conn.rollback()
finally:
    cursor.close()
    dbtemp.close(conn)

