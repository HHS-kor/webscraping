import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

for i in range(1, 6):
    #print("페이지 :", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(
        i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:
        # 광고 제거
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            #print("광고 제외\n")
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()  # 제품명
        # 애플 제외
        if "Apple" in name:
            #print("애플 제외\n")
            continue

        price = item.find(
            "strong", attrs={"calss": "price-value"})  # 가격
        if price:
            price = price.get_text()
        else:
            price = "가격 없음"

        rate = item.find("em", attrs={"class": "rating"})  # 평점
        if rate:
            rate = rate.get_text()
        else:
            #print("평점 정보 없음 제외\n")
            continue

        rate_cnt = item.find(
            "span", attrs={"class": "rating-total-count"})  # 평점 개수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]  # 출력 형태 (2)-> 괄호제거
        else:
            #print("평점 개수 없음 제외\n")
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:  # 평점 4.5이상, 평점개수 100개 이상만 출력
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*100)