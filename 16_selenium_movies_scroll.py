from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 1600x900 현재 해상도 높이인 900 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,900)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
interval = 2  # 2초 간격
while True:
    # 스크롤 가장 아래로 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 2초 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")


soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class": ["ImZGtf mpg5gc", "Vpfmgd]"]})
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})


print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print("\t<할인되지 않은 영화 제외>")
        continue

    # 할인 된 가격
    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})[
        "href"]  # 앞에 play.google.com추가해서 출력

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 :", "https://play.google.com"+link)
    print("-"*100)

browser.quit()
