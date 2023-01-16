"""
CREATE TABLE `test`.`user` (
  `no` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `sex` VARCHAR(1) NULL,
  `ssn` VARCHAR(14) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`no`));
"""

from faker import Faker
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="1234", db="test", charset="utf8")
curs = conn.cursor()

fake = Faker("ko_KR")

with open("fake_data.csv", "w", encoding="utf-8", newline='') as f:

    for _ in range(1000):
        profile = fake.profile()
        print(profile['name'], profile['sex'], profile['ssn'], profile['mail'])
        try:
            sql = "insert into user (name, sex, ssn, email)" \
                "values (%s, %s, %s, %s)"
            curs.execute(sql, (profile['name'], profile['sex'], profile['ssn'], profile['mail']))
        except:
            pass
conn.commit()
conn.close()        
