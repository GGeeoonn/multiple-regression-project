# 모듈 import
import requests
import pprint
import time


#인증키 입력
encoding = 'TL4U9WIunRjba5IMRgJgTzJPtnlvMr5tM%2BGZaF0moAtt2ZaP5L3qpU%2Bgad4%2Ffpp58OEzmg3vVTZr1Pu1HWIrpg%3D%3D'
decoding = 'TL4U9WIunRjba5IMRgJgTzJPtnlvMr5tM+GZaF0moAtt2ZaP5L3qpU+gad4/fpp58OEzmg3vVTZr1Pu1HWIrpg=='

#url 입력
url = 'http://openapi.forest.go.kr/openapi/service/forestDisasterService/frstFireOpenAPI?'
params ={'serviceKey' : decoding , 
            'pageNo' : '1', 
            'numOfRows' : '10560', 
            'searchStDt' : '19840101',
            'searchEdDt' : '20141231' }

response = requests.get(url, params=params)
time.sleep(100)

# xml 내용
content = response.text

# 깔끔한 출력 위한 코드
pp = pprint.PrettyPrinter(indent=4)
#print(pp.pprint(content))

### xml을 DataFrame으로 변환하기 ###
from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote


#bs4 사용하여 item 태그 분리
xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
rows = xml_obj.findAll('item')
print(rows)

# 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
row_list = [] # 행값
name_list = [] # 열이름값
value_list = [] #데이터값

# xml 안의 데이터 수집
for i in range(0, len(rows)):
    columns = rows[i].find_all()
    #첫째 행 데이터 수집
    for j in range(0,len(columns)):
        if i ==0:
            # time.sleep(500)
            # 컬럼 이름 값 저장
            name_list.append(columns[j].name)
        # 컬럼의 각 데이터 값 저장
        value_list.append(columns[j].text)
    # 각 행의 value값 전체 저장
    row_list.append(value_list)
    # 데이터 리스트 값 초기화
    value_list=[]

#xml값 DataFrame으로 만들기
corona_df = pd.DataFrame(row_list, columns=name_list)
print(corona_df.head(19)) 

#DataFrame CSV 파일로 저장
corona_df.to_csv('/Users/moonsung/Downloads/test/dataTest/test_parsing_data.csv', encoding='utf-8')