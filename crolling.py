# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Chrome Webdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
# 로컬환경에 설치되어 있는 크롬 버전에 맞는 드라이버를 다운로드 받는다.

path = "c:/dev/python/croller/resource/chromedriver.exe" # 적절한 경로로 수정 해 준다
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)
driver.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000002&listType=B10002")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#productListArea")))

page_results = driver.find_elements(By.CSS_SELECTOR, "li._itemSection")

for item in page_results:
    print(item.text)