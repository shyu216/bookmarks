# This is only for bookmark in firefox, other browser is not been tested yet.

import os

            
"""
example:
<DT><A HREF="https://students.unimelb.edu.au/new-students/new-student-checklist" ADD_DATE="1707008531" LAST_MODIFIED="1707187615" ICON_URI="https://students.unimelb.edu.au/__data/assets/image/0012/4587591/favicon.png" ICON="data:image/png;base64,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">New Student Checklist : The University of Melbourne</A>

to do:
1. get href, remove the query string
2. get add_date
3. append to bookmark list and return
"""
from urllib.parse import urlparse
def parse_firefox_bookmark(bookmark_path):
    bookmark = []
    with open(bookmark_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('<DT><A HREF='):
                href = line.split('HREF="')[1].split('" ADD_DATE=')[0]
                # if '?' in href:
                #     href = href.split('?')[0]
                parsed_url = urlparse(href)
                href = parsed_url.scheme + '://' + parsed_url.netloc
                add_date = line.split('ADD_DATE="')[1].split('"')[0]
                title_start = line.find('>') + 1
                title_end = line.find('</A>')
                title = line[title_start:title_end]
                # 检查href是否已经存在于书签列表中
                if not any(b['href'] == href for b in bookmark):
                    bookmark.append({'href': href, 'add_date': add_date, 'title': title})
    return bookmark


import urllib.parse
def get_full_icon_url(base_url, icon_url):
    if icon_url.startswith('http://') or icon_url.startswith('https://') or icon_url.startswith('//'):
        return icon_url
    else:
        return urllib.parse.urljoin(base_url, icon_url)
    
"""
example: 
https://students.unimelb.edu.au/new-students/new-student-checklist

use beautifulsoup to get the title/description/keywords/icon of the bookmark

note: set the encoding to utf-8 to avoid messy code
"""
import re
def clean_text(text):
    if not text: return ''
    # 替换换行符和制表符
    text = text.replace('\n', ' ').replace('\t', ' ')
    # 使用正则表达式替换多个连续空格为一个空格
    text = re.sub(' +', ' ', text)
    return text.strip()

import requests
from requests.exceptions import Timeout
import bs4
def request_info(url, timeout=10):
    try:
        r = requests.get(url, timeout=timeout)
        r.encoding = 'utf-8' 
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        title = soup.title.string
        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            description = description['content']
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords:
            keywords = keywords['content']
        icon = soup.find('link', attrs={'rel': 'icon'})
        if icon:
            icon = icon['href']
            icon = get_full_icon_url(url, icon)
        return {'title': clean_text(title), 'description': clean_text(description), 'keywords': clean_text(keywords), 'icon': icon}
    except Timeout:
        print("Request timed out")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    

import json
import os
from tqdm import tqdm
import threading
from concurrent.futures import ThreadPoolExecutor
lock = threading.Lock()  # 创建一个锁对象

def process_bookmark(b):
    global full_info
    if not any(info['href'] == b['href'] for info in full_info):
        info = request_info(b['href'])
        print(info)
        if info:
            with lock:  # 使用锁来同步写入文件的操作
                if not any(info['href'] == b['href'] for info in full_info):  # 再次检查以避免重复添加
                    full_info.append({'href': b['href'], 'add_date': b['add_date'], 'title': info['title'], 'description': info['description'], 'keywords': info['keywords'], 'icon': info['icon']})
                    tqdm.write(f"Processed bookmark: {b['href']}")  # 打印处理的书签信息
                    with open('bookmark.json', 'w', encoding='utf-8') as f:
                        json.dump(full_info, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    bookmark_path = os.path.expanduser('./bookmarks.html')
    bookmark = parse_firefox_bookmark(bookmark_path)
    full_info = []
    if os.path.exists('bookmark.json'):
        with open('bookmark.json', 'r', encoding='utf-8') as f:
            full_info = json.load(f)

    with ThreadPoolExecutor(max_workers=8) as executor:
        list(tqdm(executor.map(process_bookmark, bookmark), total=len(bookmark), desc="Processing bookmarks"))