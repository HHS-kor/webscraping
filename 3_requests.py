import requests
res = requests.get("http://google.com")
res.raise_for_status()  # 여기서 오류를 발생시키고 중단

# print("응답코드 :", res.status_code)  # 200 정상

# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("에러코드", res.status_code)

print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
