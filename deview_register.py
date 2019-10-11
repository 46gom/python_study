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
driver.get("https://deview.kr/2019/register")
endCheck = True
while endCheck:
    try:
        if len(driver.find_element_by_class_name("register_btn")) > 0:
            driver.find_element_by_class_name("register_btn").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#privacyAgree")))
            driver.find_element_by_id("name").send_keys("김정환")
            driver.find_element_by_id("email").send_keys("vitokim@naver.com")
            driver.find_element_by_id("job").send_keys("CJ 올리브영")
            driver.find_element_by_id("privacyAgree").click()
            driver.find_element_by_id("submit").click()
            endCheck = True
        else:
            driver.refresh()
    except:
        driver.refresh()
        pass
    
