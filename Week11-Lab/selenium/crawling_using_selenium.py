from bs4 import BeautifulSoup
from selenium import webdriver
import time

# url = "http://v.media.daum.net/v/20161103113844417"
url = "http://v.media.daum.net/v/20161120134647462"

driver = webdriver.Firefox()
driver.get(url)

found_element = True
while found_element:
    try:
        element = driver.find_element_by_xpath("//div[@class='alex_more']")
        # 더보기 버튼의 요소 class="alex_more"
        # xpath: html 소스를 분석해서 특정 요소를 찾는 방법 중 하나. 
        # 계층에 따라 h1//a//div와 같은 형식으로 path를 구분
        element.click() # element를 계속 클릭해주고
        time.sleep(3)
        # 한번 클릭하면 3초 쉼. 더보기를 계속 누르면 안 되고, next page가 로딩될 때까지 기다려줘야 하므로
        # 대부분의 웹사이트를 수집할 수 있는 장점, 그러나 조금 오래 걸린다는 단점
 
    except Exception:
        found_element = False # 이때까지 while문을 계속 돌림

# 페이지 로딩이 끝나면 다음부터는 그냥 BS 사용
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

comments = soup.find_all("ul", class_="list_comment")
print(comments)
