"""
Tesseract 다운로드
https://tesseract-ocr.github.io/tessdoc/Installation.html

윈도우 OS 사용자의 경우 아래 링크에서 다운받으세요.
https://github.com/UB-Mannheim/tesseract/wiki
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.0.20221222.exe

OS에 맞는 설치 파일을 다운로드 후 설치하세요.

설치 후 Tesseract 설치 경로를 Path에 추가합니다.
Tesseract 설치 경로 기본값: C:\Program Files\Tesseract-OCR
Path 설치 방법: https://blog.naver.com/oralol/222472012941

[파이썬]
* opencv 설치: pip install opencv-python
* pytesseract 설치: pip install pytesseract
pip 실행이 안될 경우 python -m pip 으로 해보시기 바랍니다.

* OEM(OCR Engine Mode)
0 레거시 엔진
1 신경망 LSTM 엔진
2 레거시+LSTM
3 기본값

* PSM(Page Segmentation Mode)
0 방향 및 스크립트 감지(OSD) 전용.
1 OSD를 통한 자동 페이지 분할.
2 자동 페이지 분할, OSD 또는 OCR 없음.
3 완전 자동 페이지 분할이지만 OSD는 없습니다. (기본값)
4 다양한 크기의 단일 텍스트 열을 가정합니다.
5 세로로 정렬된 텍스트의 단일 균일 블록을 가정합니다.
6 하나의 균일한 텍스트 블록을 가정합니다.
7 이미지를 단일 텍스트 줄로 처리합니다.
8 이미지를 한 단어로 취급합니다.
9 이미지를 원 안의 한 단어로 취급합니다.
10 이미지를 단일 문자로 처리합니다.
11 희소 텍스트. 특정 순서 없이 가능한 한 많은 텍스트를 찾습니다.
12 OSD가 포함된 희소 텍스트.
13 원시 라인. 이미지를 단일 텍스트 줄로 취급하여 Tesseract에 특정한 핵을 우회합니다.
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = cv2.imread('test.png')
my_config = "-l eng+kor --oem 3 --psm 6"
# my_config = "--oem 3 --psm 6 outputbase digits"
# my_config = "-c tessedit_char_whitelist=0123456789 --oem 3 --psm 6"
# my_config = "-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --oem 3 --psm 6"
# my_config = "-c tessedit_char_blacklist=0123456789 --oem 3 --psm 6"
result = pytesseract.image_to_string(img, config=my_config)
print(result)
