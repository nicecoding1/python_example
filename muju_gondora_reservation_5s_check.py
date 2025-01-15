import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jmunja import smssend
import time  # 추가된 모듈


# 예약 사이트 URL
URL = "https://www.mdysresort.com/gondora/res_gon1.asp?"


# 예약 상태 확인 함수
def check_availability():
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        reservation_elements = soup.select("#res_gon1 > div > div.cal_con > div.calendar_box > div:nth-child(4) > ul.sat > li.res")

        for element in reservation_elements:
            if "매진" not in element.text:
                return True  # 예약 가능 상태 발견
        return False  # 모든 항목이 매진 상태
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# SMS 보내기 함수 (제이문자)
def send_sms_notification():
    uid = ""
    upw = ""
    subject = "곤도라예약"
    content = "곤도라 예약이 가능합니다! 지금 바로 사이트를 방문하세요: " + URL,

    jphone = smssend.JmunjaPhone(uid, upw)
    result = jphone.send(subject, content, "01012345678")

    if result:
        print("SMS 발송 완료")


# 메인 함수
def main():
    while True:
        if check_availability():
            print("예약 가능 상태 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            send_sms_notification()
            time.sleep(30)
        else:
            print("모든 예약이 매진 상태입니다.")
            pass
        time.sleep(5)

if __name__ == "__main__":
    main()
