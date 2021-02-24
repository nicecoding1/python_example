import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='db_user', password='db_password',
                       db='db_name', charset='utf8')
curs = conn.cursor()

resp = requests.get('https://www.yna.co.kr/news')
resp.raise_for_status()

resp.encoding = 'utf-8'
html = resp.text

bs = BeautifulSoup(html, 'html.parser')

for i in range(1, 27, 1):
    if i == 6: # 광고 생략
        continue
    tags = bs.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child('
                     + str(i) + ')')
    _date = bs.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child('
                    + str(i) + ') > div > div.info-box01 > span.txt-time')
    _img = bs.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child('
                     + str(i) + ') > div > figure > a > img ')
    _title = bs.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child('
                       + str(i) + ') > div > div.news-con > a > strong')
    _content = bs.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child('
                       + str(i) + ') > div > div.news-con > p')

    try:
        _imgsrc = _img[0]['src']
    except:
        _imgsrc = ""

    _d = _date[0].getText()
    _i = _imgsrc
    _t = _title[0].getText()
    _c = _content[0].getText()

    sql = """
    insert IGNORE into news (news_date, news_img, news_title, news_content) 
    values (%s, %s, %s, %s)"""
    curs.execute(sql, (_d, _i, _t, _c))

conn.commit()
conn.close()

"""
MySQL 테이블 생성문
CREATE TABLE `news` (
  `no` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `news_date` date DEFAULT NULL,
  `news_img` varchar(200) DEFAULT NULL,
  `news_title` varchar(50) DEFAULT NULL,
  `news_content` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`no`),
  UNIQUE KEY `Index1` (`news_date`,`news_title`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

"""
