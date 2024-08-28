# This is only for bookmark in firefox, other browser is not been tested yet.

import os

import requests
from requests.exceptions import Timeout
import bs4
            
import urllib.parse

import re


import json
from tqdm import tqdm
import threading
from concurrent.futures import ThreadPoolExecutor

"""
to do:
1. get href, remove the query string
2. get add_date
3. append to bookmark list and return
"""
def parse_firefox_bookmark(bookmark_path):
    bookmark = []
    with open(bookmark_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('<DT><A HREF='):
                href = line.split('HREF="')[1].split('" ADD_DATE=')[0]

                # Query里面是否含有隐私信息？
                # if '?' in href:
                #     href = href.split('?')[0]

                add_date = line.split('ADD_DATE="')[1].split('"')[0]
                title_start = line.find('>') + 1
                title_end = line.find('</A>')
                title = line[title_start:title_end]
                # 检查href是否已经存在于书签列表中
                if not any(b['href'] == href for b in bookmark):
                    bookmark.append({'href': href, 'add_date': add_date, 'title': title})
    return bookmark


def get_full_icon_url(base_url, icon_url):
    if icon_url.startswith('http://') or icon_url.startswith('https://'):
        icon = icon_url
    elif icon_url.startswith('//'):
        icon = 'http:' + icon_url
    else:
        icon = urllib.parse.urljoin(base_url, icon_url)
    icon_response = requests.get(icon)
    if icon_response.status_code == 200:
        content_type = icon_response.headers.get('Content-Type')
        if content_type and 'image/x-icon' in content_type:
            return icon
        else:
            return None
    else:
        return None
    
    
def clean_text(text):
    if not text: return None
    # 替换换行符和制表符
    text = text.replace('\n', ' ').replace('\t', ' ')
    # 使用正则表达式替换多个连续空格为一个空格
    text = re.sub(' +', ' ', text)
    return text.strip()


"""
to do:
use beautifulsoup to get the source code
"""
def request_info(url, timeout=10000):
    try:
        # 一些网站需要头（10+），一些不需要（100+），大部分是都行（1000）
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        #     'Connection': 'keep-alive','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.9',
        #     'Accept-Encoding': 'gzip, deflate, br',
        # }
        # r = requests.get(url, timeout=timeout, headers=headers)
        r = requests.get(url, timeout=timeout) #, headers=headers)
        if r.encoding == 'ISO-8859-1':
            r.encoding = 'utf-8'  
        soup = bs4.BeautifulSoup(r.text, 'html.parser', from_encoding="gb18030")
                
        # 尝试从 <title> 标签中获取标题
        title = soup.title.string if soup.title else None

        # 如果 <title> 标签不存在，尝试从 <meta> 标签中获取标题
        if not title:
            meta_tag = soup.find('meta', attrs={'property': 'og:title'})
            title = meta_tag['content'] if meta_tag else None

        if not title:
            meta_tag = soup.find('meta', attrs={'name': 'twitter:title'})
            title = meta_tag['content'] if meta_tag else None

        # 如果 <meta> 标签也不存在，尝试从 <h1> 标签中获取标题
        if not title:
            h1_tag = soup.find('h1')
            title = h1_tag.string if h1_tag else None

        if not title:
            print(f"Title not found: {url}")
            return None



        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            description = description['content']

        if not description:
            meta_tag = soup.find('meta', attrs={'name': 'Description'})
            description = meta_tag['content'] if meta_tag else None

        if not description:
            meta_tag = soup.find('meta', attrs={'property': 'og:description'})
            description = meta_tag['content'] if meta_tag else None

        if not description:
            meta_tag = soup.find('meta', attrs={'name': 'twitter:description'})
            description = meta_tag['content'] if meta_tag else None

        if not description:
            description = None
        
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords:
            keywords = keywords['content']

        if not keywords:
            keywords = None


        icon = soup.find('link', attrs={'rel': 'icon'})
        if icon:
            icon = icon['href']
        else:
            icon = '/favicon.ico'
        icon = get_full_icon_url(url, icon)

        raw_text = soup.get_text()
        raw_text = raw_text.replace('\n', ' ').replace('\t', ' ')
        raw_text = re.sub(' +', ' ', raw_text)
        raw_text = raw_text[:1000]

        return {
            'title': clean_text(title), 
            'description': clean_text(description), 
            'keywords': clean_text(keywords), 
            'icon': icon, 
            'raw_text': raw_text
            }
    except Timeout:
        print(f"Timeout: {url}")
        return None
    except Exception as e:
        print(f"*** {e}: {url}")
        return None
    

lock = threading.Lock()  # 创建一个锁对象

def process_bookmark(b):
    global full_info
    if not any(info['href'] == b['href'] for info in full_info):
        info = request_info(b['href'])
        # print(info)
        with lock:  # 使用锁来同步写入文件的操作
            if info:
                if True: # not any(info['href'] == b['href'] for info in full_info):  # 再次检查以避免重复添加
                    if info["title"] is None:
                        with open('error.txt', 'a', encoding='utf-8') as f:
                            f.write(f"{b['href']}\n")
                    else:
                        full_info.append({'href': b['href'], 'add_date': b['add_date'], 'title': info['title'], 'description': info['description'], 'icon': info['icon'], 'raw_text': info['raw_text']})
                        # tqdm.write(f"Processed bookmark: {b['href']}")  # 打印处理的书签信息
                        with open('sites.json', 'w', encoding='utf-8') as f:
                            json.dump(full_info, f, indent=4, ensure_ascii=False)
            else:
                with open('error.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{b['href']}\n")

if __name__ == '__main__':
    bookmark_path = os.path.expanduser('./bookmarks.html')
    bookmark = parse_firefox_bookmark(bookmark_path)
    full_info = []
    if os.path.exists('sites.json'):
        with open('sites.json', 'r', encoding='utf-8') as f:
            full_info = json.load(f)

    with ThreadPoolExecutor(max_workers=16) as executor:
        # list(tqdm(executor.map(process_bookmark, bookmark), total=len(bookmark), desc="Processing bookmarks"))
        list(executor.map(process_bookmark, bookmark))