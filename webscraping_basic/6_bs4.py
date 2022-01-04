import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
# headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
res = requests.get(url) # , headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 우리가 가져온 html 문서 (res.text) 를 lxml 파서를 통해서 BeautifulSoup 객체로 만듦
# soup 은 모든 정보를 가지고 있음
# print(soup.title)
# print(soup.title.get_text()) # soup 객체에서 처음 발견되는 title element 의 텍스트만 가져옴
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element 의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 href 속성의 "값" 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # soup 객체에서 find 함수로 속성 attrs={"class":"Nbtn_upload"} 와 일치하는 첫 번째 a element 출력
# print(soup.find(attrs={"class":"Nbtn_upload"})) # soup 객체에서 find 함수로 속성 attrs={"class":"Nbtn_upload"} 와 일치하는 첫 번째 element 출력
# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"}) # soup 객체에서 속성 attrs={"class":"rank01"}인 li element 반환
# print(rank1.a.get_text()) # rank1 객체의 자식 a element 의 텍스트만 출력
# print(rank1.next_sibling) # rank1 객체의 다음 형제 element 출력
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # rank3 객체의 이전(개행)+이전 형제 element 출력
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # rank1 객체의 다음 형제 element 를 개행 무시하고 출력
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") # rank3 객체의 이전 형제 element 를 개행 무시하고 출력
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="백수세끼-108화 딸기 초코케이크") # soup 객체에서 find 함수로 속성 text="백수세끼-108화 딸기 초코케이크" 와 일치하는 첫 번째 a element 출력
print(webtoon)