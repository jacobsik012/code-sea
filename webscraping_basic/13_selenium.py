from selenium import webdriver
import time

browser = webdriver.Chrome() # "./chromedriver.exe" : 현재 폴더에 있는 chromedriver.exe 를 의미
# 크롬 웹드라이버 객체를 생성해서(browser), 브라우저에서 get(url) 로 이동

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
# browser = driver

# browser.get("http://naver.com")

# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()
# elem = browser.find_element_by_id("query")

# from selenium.webdriver.common.keys import Keys

# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_elements_by_tag_name("a") # 리스트로 반환
# for e in elem:
#     e.get_attribute("href")
#     print(e)

# browser.get("http://daum.net")
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# browser.back()

# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]') 
# elem.click()
# browser.quit()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
elem = browser.find_element_by_id("id").send_keys("naver_id")
elem = browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
elem = browser.find_element_by_id("log.login").click()

time.sleep(1)

# 5. id 를 새로 입력
elem = browser.find_element_by_id("id").clear()
elem = browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료

