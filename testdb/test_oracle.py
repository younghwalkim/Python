# path : testdb\\test_oracle.py
# 파이썬과 오라클 연동 처리

# 오라클사에서 제공하는 파이썬과 오라클을 연동하기 위한 드라이버 파일 다운로드 및 설치
# https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
# windows 64bit zip , 18 version
# D:\\ 폴더에 이동

# 1. 사용할 패키지(모듈) 임포트함
import cx_Oracle
import os

# 2. 오라클 드라이브(instantclient) 등록
# 방법 1 : 환경변수 path 에 등록 (파이썬 코드로 등록할 수 있음)
location  ='D:\\instantclient_18_5'
os.environ['PATH']  = location + ';' + os.environ['PATH']

# 방법 2 : 코드로 오라클 초기 설정으로 지정.
# 주의 :  애플리케이션 전체 실행시 한번만 구동되어야 함.
cx_Oracle.init_oracle_client(lib_dir=location)

# 3. 데이터베이스 연결
dbUrl = 'localhost:1521/xe'
dbUser = 'c##testweb'
dbPass = 'testweb'

conn = cx_Oracle.connect(dbUser, dbPass, dbUrl)
# conn = cx_Oracle.connect('c##testweb','testweb','localhost:1521/xe')
# conn = cx_Oracle.connect('c##testweb/testweb@localhost:1521/xe')
print('conn : ', conn)

# 4. 쿼리문 준비
query = 'select * from member'

# 5. 쿼리문 실행시키기 위한 객체 준비, 실행 처리
cursor = conn.cursor()
cursor.execute(query)

# 커서가 실행된 쿼리문의 결과를 받음.
# select 쿼리문을 실행시켰다면, 결과집합(ResultSet)을 커서가 받음
# dml 문(insert, update, delete) 은 처리된 행갯수를 커서가 받음
print('cursor : ', cursor)

# 6. select 쿼리문이라면 실행결과에 대한 매핑 작업

# 커서가 가진 결과 정보를 꺼내서 변수에 옮겨 기록 저장 처리.
# result = cursor.fetchall()
# print('result : ', result)
# print('type : ', type(result))
# print('count : ',len(result))
# for record in result :
# 	print(record)

# 커서가 가진 select 쿼리조회결과를 한 행씩 1개씩 출력
for row in cursor :
    # print('행이 가진 컬럼 갯수 : ', len(row), type(row))
    # print(row)

    # 컬럼별로 데이터 하나씩 추출
    userid = row[0]
    userpwd = row[1]
    username = row[2]
    gender = row[3]
    age = row[4]
    phone = row[5]
    email = row[6]
    ENROLL_DATE = row[7]
    LASTMODIFIED = row[8]
    SIGNTYPE = row[9]
    ADMIN_YN = row[10]
    LOGIN_OK = row[11]
    PHOTO_FILENAME = row[12]

    # print(userid, userpwd, username)

    # index 를 이용한 출력 처리
    for i in range(len(row)):
        print(row[i], end=', ')
    print()

# 작업이 끝나면 받드시 닫음.
cursor.close()
conn.close()