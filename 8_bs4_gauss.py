import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class": "title"})

# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

#만화제목 + 링크
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)

# 평점
total_rates = 0
car_star = soup.find_all("div", attrs={"class": "rating_type"})
for car in car_star:
    rate = car.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체점수 : ", total_rates)
print("평균점수 :", total_rates / len(car_star))
