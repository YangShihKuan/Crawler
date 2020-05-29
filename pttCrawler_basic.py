# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:11:35 2020

@author: Hsun Jung Chen
"""



import requests

def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !
    return response

url = 'https://www.ptt.cc/bbs/movie/index.html'
resp = fetch(url)  # step-1

print(resp.text) # result of setp-1


from requests_html import HTML

def parse_article_entries(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent')
    return post_entries

url = 'https://www.ptt.cc/bbs/movie/index.html'
resp = fetch(url)  # step-1
post_entries = parse_article_entries(resp.text)  # step-2

print(post_entries)  # result of setp-2

def parse_article_meta(entry):
    '''
    每筆資料都存在 dict() 類型中：key-value paird data
    '''
    return {
        'title': entry.find('div.title', first=True).text,
        'push': entry.find('div.nrec', first=True).text,
        'date': entry.find('div.date', first=True).text,
        'author': entry.find('div.author', first=True).text,
        'link': entry.find('div.title > a', first=True).attrs['href'],
    }

url = 'https://www.ptt.cc/bbs/movie/index.html'
resp = fetch(url)  # step-1
post_entries = parse_article_entries(resp.text)  # step-2

for entry in post_entries:
    meta_article = parse_article_meta(entry)
    print(meta_article)  # result of setp-3

    # pretty_print(meta['push'], meta['title'], meta['date'], meta['author'])  # for below results