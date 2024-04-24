import loop.forSample as lf
import loop.whileSample as lw
import mission.forMission as mf

import cv2 as cv
import sys

# 프로그램을 시작하는 구문임
if __name__ == '__main__':
    # lf.test_for1()
    # lf.test_for2()

    # lf.test_Iterable()

    # lf.test_range()

    # 입력 단수 출력
    # lf.test_indexing()

    # 2단~9단
    # lf.print_gugudan()

    # lf.doubleFor()

    # lf.list_in_list1()
    # lf.list_in_list2()
    # lf.list_in_list3()

    # mf.practice()

    # lw.test_while()
    # lw.print_unicode1()
    # lw.print_unicode2()

    # lw.display_menu()

    # 이미지 호출
    img = cv.imread('1.jpeg')

    # 이미지 흑백 처리
    gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # 흑백 이미지 축소 처리 (50%) ,
    gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

    # 원본
    cv.imshow('Image Display', img)

    # 흑백 이미지
    cv.imwrite(('1.jpg'), gray)
    cv.imshow('gray img', gray)

    #  축소 이미지
    cv.imwrite('1.jpg', gray_small)
    cv.imshow('small img', gray_small)

    # 키 입력 대기
    cv.waitKey()
    cv.destroyAllWindows()


