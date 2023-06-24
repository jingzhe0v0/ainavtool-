import re
import sys
import urllib.request,urllib.error
import sqlite3
from bs4 import BeautifulSoup
import xlwt
import time
import requests
from lxml import etree

baseurl="https://ainavtool.com/ai%e5%bf%ab%e8%ae%af/page/"

head={
        "user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54"
    }

page_list=[baseurl+str(i) for i in range(1,20)]

for page in page_list :
    html=requests.get(url=page).text
    tree=etree.HTML(html)
    url_list=tree.xpath('//div[@class="cat_list"]//div[@class="list-body"]/h2/a/@href')
    for url in url_list:
        art_html=requests.get(url=url).text
        art_tree=etree.HTML(art_html)
        title=art_tree.xpath('//div[@class="panel card"]/div/div/h1/text()')
        passage_list=art_tree.xpath('//div[@class="panel-body single mt-2"]/p/text()')
        text=''
        for passage in passage_list :
            text=text+passage
        with open('最新资讯.txt','a',encoding='utf-8') as file:
            file.write('\n\n\n************************************************'+title[0]+'************************************************\n\n'+text) 
