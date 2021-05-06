import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 반환
# print(soup.a.attrs)  # a element의 속성 정보 반환
# print(soup.a["href"])  # a element의 href 속성 '값' 정보 반환

print(soup.find("a", attrs={"class": "Nbtn_upload"}))
print(soup.find(attrs={"class": "Nbtn_upload"}))
# 1:16:04
