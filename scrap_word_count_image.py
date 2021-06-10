# Python 3.6.8 64-bit

import time
from bs4 import BeautifulSoup
import requests
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 스크래핑
url = "https://healthguides.cnn.com/finding-the-right-migraine-treatment/how-to-ensure-your-doctor-understands-your-migraine-severity"
webpage = requests.get(url) 
soup = BeautifulSoup(webpage.content, "html.parser")
item = soup.select_one("article.ArticlePage-mainContent")
data = item.text

# 단어 분리
word = str(data).lower().strip().split()
count = Counter(word).most_common()
words = dict(count)
# print(words)

# 워드클라우드
wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\Gothic.ttf',
                      background_color="white", max_font_size=100).generate_from_frequencies(words)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
