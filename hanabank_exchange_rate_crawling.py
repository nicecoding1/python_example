#!/usr/bin/env python
# coding: utf-8

# In[29]:


get_ipython().system('pip install selenium==4.1.5')
get_ipython().system('pip install webdriver_manager')

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # chromedriver 자동설치
from webdriver_manager.chrome import ChromeDriverManager #chromedriver 자동설치
from selenium.webdriver.common.by import By
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# In[36]:


# 인터넷 열기
driver = webdriver.Chrome(service=service)


# In[43]:


# 원하는 사이트 접속
driver.get('https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp?_menuNo=23100&#35;//HanaBank')


# In[46]:


# 원하는 요소를 찾기
driver.find_element(By.CLASS_NAME, "tblBasic.leftNone")

