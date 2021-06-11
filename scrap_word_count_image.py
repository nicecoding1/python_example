# Python 3.6.8 64-bit

import time
from bs4 import BeautifulSoup
import requests
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re
from collections import Counter

# 스크래핑
url = "https://healthguides.cnn.com/finding-the-right-migraine-treatment/how-to-ensure-your-doctor-understands-your-migraine-severity"
webpage = requests.get(url) 
soup = BeautifulSoup(webpage.content, "html.parser")
item = soup.select_one("article.ArticlePage-mainContent")
data = str(item.text).lower()

# 단어 분리
nltk.download('all')
cleaned_data = re.sub(r'[^\.\?\!\w\d\s]','',data)
words = nltk.word_tokenize(cleaned_data)
tokens_pos = nltk.pos_tag(words)

NN_words = []
for word, pos in tokens_pos:
    if 'NN' in pos:
        NN_words.append(word)
c = Counter(NN_words)

# 워드클라우드
wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\Gothic.ttf',
                      background_color="white", max_font_size=100).generate_from_frequencies(c)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
wordcloud.to_file("wordcloud.png")
