# hellocv.py
# opencv 패키지 설치 : opencv_python
# opencv 모듈명 : cv2
import cv2
import sys

# print(cv2.__version__)

# 시스템 기본 카메라부터 cv2.VideoCapture 객체 생성함.
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 카메라와 연결 시도

# 카메라 열기 실패
if not cap.isOpened():
    print('카메라 연결 실패')
    sys.exit()  # 프로그램 종료

# 카메라 프레임 해상도 출력
print('Frame width : ', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height : ', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 매프레임 처리 및 화면 출력
while True:
    ret, frame = cap.read()  # 비디오를 구성하는 프레임 획득
    # frame : 카메라로 부터 읽은 프레임 정보 저장
    # ret (return) : 읽기 성공 여부 저장 (True |False)
    # 다른 앱(zoom 등)에서 카메라 사용중(on)이면 작동 안됨.

    if not ret:     # if  ref == False 과 같음
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break       # 반복 종료

    # 경계선 검출 함수 :  이미지의 경계선만 리턴함
    edge = cv2.Canny(frame, 50, 150)
    # cv2.Canny(프레임, threshold1, threshold2)
    # threshold1 : minVal 임계값 (값이 크면 엣지 검출이 어렵고, 작을수록 엣지 검출이 쉽다)
    #                   적으면 경계선이 이어짐, 크면 경계선이 끊어짐
    # threshold2 : maxVal 임계값 (경계선인지 아닌지를 판단하는 임계값임. 작을수록 엣지가 많아짐)
    # edge = cv2.Canny(frame, 150, 150)
    # edge = cv2.Canny(frame, 50, 50)

    cv2.imshow('edge', edge)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1)  == 27: #  esc  키 누르면 종료
        break

cap.release()  # 카메라와 연결을 끊음
cv2.destroyAllWindows()



