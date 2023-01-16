from faker import Faker
import csv

fake = Faker("ko_KR")

with open("fake_data.csv", "w", encoding="utf-8", newline='') as f:
    wr = csv.writer(f)
    for _ in range(10000):
        profile = fake.profile()
        print(profile['name'], profile['sex'], profile['ssn'], profile['mail'])
        wr.writerow([profile['name'], profile['sex'], profile['ssn'], profile['mail']])
