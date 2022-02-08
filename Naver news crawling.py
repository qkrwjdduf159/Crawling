import requests
from bs4 import BeautifulSoup

## 검색어 입력
search = input('검색할 키워드를 입력해주세요.')

## 검색할 페이지 입력
page = int(input('크롤링할 페이지를 입력해주세요.')) #ex) 숫자만 입력이 가능합니다.
print('크롤링할 페이지 :', page, '페이지')

## start수를 1, 11, 21, 31, ... 만들어 주는 함수
page_num = 0

if page == 1:
    page_num = 1
elif page == 0:
    page_num = 1
else:
    page_num = page + 9*(page - 1)

## url 생성
url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search}&start={str(page_num)}'

## html 불러오기
original_html = requests.get(url)
html = BeautifulSoup(original_html.text, 'html.parser')

# 검색결과
articles = html.select("div.group_news > ul.list_news > li div.news_area > a")
print(articles)
# 검색된 기사의 갯수
print(len(articles),"개의 기사가 검색됌.")

## 뉴스기사 제목 가져오기
news_title = []
for i in range(len(articles)):
    news_title.append(articles[i]['title'])
print(news_title)

## 뉴스기사 URL 가져오기
news_url = []
for i in range(len(articles)):
    news_url.append(articles[i]['href'])
print(news_url)