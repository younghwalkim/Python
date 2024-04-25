import cv2 as cv
import sys

def ch_2_3():
    # 이미지 호출
    img = cv.imread('img_face.jpeg')

    if img is None:
        sys.exit('파일을 찾을 수 없습니다.')

    # 이미지 흑백 처리
    gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # 흑백 이미지 축소 처리 (50%) ,
    gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)

    # 원본
    cv.imshow('Image Display', img)

    # 흑백 이미지
    cv.imwrite(('img_face_gray.jpg'), gray)
    cv.imshow('gray img', gray)

    #  축소 이미지
    cv.imwrite('img_face_small.jpg', gray_small)
    cv.imshow('small img', gray_small)

    # 키 입력 대기
    cv.waitKey()
    cv.destroyAllWindows()

def ch_2_6():
    img = cv.imread('img_laughing.jpg')

    if img is None:
        sys.exit('파일을 찾을 수 없습니다.')

    # cv.rectangle(img, (830, 30), (1000, 200), (0, 0, 255), 2)  # 직사각형 그리기
    cv.rectangle(img, (830, 30), (1000, 200), (0, 0, 255), 2)  # 직사각형 그리기
    cv.putText(img, 'laugh', (830, 24), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # 글씨 쓰기

    cv.imshow('Draw', img)

    cv.waitKey()
    cv.destroyAllWindows()

def ch_2_7():
    img = cv.imread('img_laughing.jpg')

    if img is None:
        sys.exit('파일을 찾을 수 없습니다.')

    def draw(event, x, y, flags, param):  # 콜백 함수
        if event == cv.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 클릭했을 때
            cv.rectangle(img, (x, y), (x + 200, y + 200), (0, 0, 255), 2)
        elif event == cv.EVENT_RBUTTONDOWN:  # 마우스 오른쪽 버튼 클릭했을 때
            cv.rectangle(img, (x, y), (x + 100, y + 100), (255, 0, 0), 2)

        cv.imshow('Drawing', img)

    cv.namedWindow('Drawing')
    cv.imshow('Drawing', img)

    cv.setMouseCallback('Drawing', draw)  # Drawing 윈도우에 draw 콜백 함수 지정

    while (True):  # 마우스 이벤트가 언제 발생할지 모르므로 무한 반복
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

def ch_2_8():
    img = cv.imread('img_soccer.jpg')

    if img is None:
        sys.exit('파일을 찾을 수 없습니다.')

    def draw(event, x, y, flags, param):
        global ix, iy

        if event == cv.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
            ix, iy = x, y
        elif event == cv.EVENT_LBUTTONUP:  # 마우스 왼쪽 버튼 클릭했을 때 직사각형 그리기
            cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)

        cv.imshow('Drawing', img)

    cv.namedWindow('Drawing')
    cv.imshow('Drawing', img)

    cv.setMouseCallback('Drawing', draw)

    while (True):
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break



def ch_2_9():
    img=cv.imread('img_soccer.jpg')

    if img is None:
        sys.exit('파일을 찾을 수 없습니다.')

    BrushSiz=5					# 붓의 크기
    LColor,RColor=(255,0,0),(0,0,255)		# 파란색과 빨간색

    def painting(event,x,y,flags,param):
        if event==cv.EVENT_LBUTTONDOWN:
            cv.circle(img,(x,y),BrushSiz,LColor,-1)# 마우스 왼쪽 버튼 클릭하면 파란색
        elif event==cv.EVENT_RBUTTONDOWN:
            cv.circle(img,(x,y),BrushSiz,RColor,-1)# 마우스 오른쪽 버튼 클릭하면 빨간색
        elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
            cv.circle(img,(x,y),BrushSiz,LColor,-1)# 왼쪽 버튼 클릭하고 이동하면 파란색
        elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
            cv.circle(img,(x,y),BrushSiz,RColor,-1)# 오른쪽 버튼 클릭하고 이동하면 빨간색

        cv.imshow('Painting',img)		# 수정된 영상을 다시 그림

    cv.namedWindow('Painting')
    cv.imshow('Painting',img)

    cv.setMouseCallback('Painting',painting)

    while(True):
        if cv.waitKey(1)==ord('q'):
            cv.destroyAllWindows()
            break

# 프로그램을 시작하는 구문임
if __name__ == '__main__':
    
    # 이미지 색깔, 크기 변화
    # ch_2_3()
    
    #  사진의 웃는표정에 Box에 표시
    # ch_2_6()
    
    #  사진에 Box 표시하기
    # ch_2_7()

    # 사진에 Box 그리기
    # ch_2_8()

    # 사진에 점선 그리기
    ch_2_9()
