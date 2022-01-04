import requests
from bs4 import BeautifulSoup

for year in range(2016, 2021):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"}) # list 로 반환하기 때문에 ["src"] 를 못 붙임
    for idx, image in enumerate(images):
        image_url = image["src"]
        # if not "http://" in image_url:
        #     image_url = "http://" + image_url
        if image_url.startswith("//"): # startswith : image_url 이 "//" 로 시작한다면
            image_url = "http://" + image_url

        print(image_url)
        image_res = requests.get(image_url) # image_url 주소의 html 데이터를 전부 get
        image_res.raise_for_status()

        with open("movie_{0}_{1}.jpg".format(year, idx + 1), "wb") as f: # 만들어 열고자 하는 파일 (화상메모리) 이 text 가 아니라 binary
            f.write(image_res.content) # image_res 가 가지고 있는 content 정보 (여기서는 이미지) 를 찾아서 써줌
        
        if idx >= 4:
            break

