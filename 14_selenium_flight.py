# 3.22.45
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)  # 주소로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click()  # [0]-->이번달
# browser.find_elements_by_link_text("28")[0].click()

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click()  # [1]-->다음달
# browser.find_elements_by_link_text("28")[1].click()

# 이번 달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click()  # [0]-->다음달
browser.find_elements_by_link_text("28")[1].click()  # [1]-->다음달

# 제주도 선택
browser.find_element_by_xpath(
    "/html/body/div/div/div[2]/div[2]/div/div[2]/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 로딩 대기 / 최대 10초까지 기다리되, 해당 xpath의 element가 나타나면 다음 동작 실행
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((
        By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)  # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath(
#     "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
