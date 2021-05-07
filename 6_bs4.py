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

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))  # a엘리먼트
# print(soup.find(attrs={"class": "Nbtn_upload"}))  # 아무 엘리먼트
# 1:16:04
# print(soup.find("li", attrs={"class": "rank01"}))
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")  # 개행 상관없이 찾아준다 //find_previous_sibling()
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# print(rank1.find_next_siblings("li"))  # li 태그인 다음 형제들 모두 가져옴
webtoon = soup.find("a", text="재혼 황후-80화")
print(webtoon)
