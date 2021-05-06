import requests
url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nodocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
