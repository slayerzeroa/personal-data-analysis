import requests
import time

from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_blog_rank():

    # 웹드라이버 설정
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)

    # 사이트 접속
    driver.get("https://www.blogchart.co.kr/chart/week")
    driver.implicitly_wait(10)

    # 카테고리
    table = driver.find_element(By.CLASS_NAME, "Category_list_table")
    table.find_element(By.XPATH, "//a[text()='금융 | 재테크']").click()
    driver.implicitly_wait(10)

    # 블로그 순위 링크 가져오기
    table = driver.find_element(By.CLASS_NAME, "all_category")
    blog_rank = table.find_elements(By.CLASS_NAME, "week_blog_URl")
    driver.implicitly_wait(10)

    blog_list = []
    # for blog in blog_rank:
    for blog in blog_rank:
        blog_list.append(bs(blog.get_attribute('outerHTML'), 'html.parser').find('a')['href'])

    return(list(set(blog_list)))


print(get_blog_rank())