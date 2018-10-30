import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)"
                  "AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
}


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '科技',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url, headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_news(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            author = item.get('media_name')
            author_id = item.get('id')
            comments = item.get('comments_counts')
            contents = item.get('article_url')
            date = item.get('date')
            images = item.get('image_list')
            title = item.get('abstract')
            new_id = item.get('item_id')
            yield {
                'author': author,
                'author_id': author_id,
                'comments': comments,
                'contents': contents,
                'date': date,
                'images': images,
                'title': title,
                'new_id': new_id
            }


def save_news(item):
    # print(item)
    with open('data.json', 'a', encoding='utf-8') as f:
        data = json.dumps(item, ensure_ascii=False)
        f.write(data)
        # print(data)


def main(offset):
    print('正在保存第%d页信息' % (offset/20))
    json = get_page(offset)
    for item in get_news(json):
        # print(item)
        save_news(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    print('保存完成！')
    pool.close()
    pool.join()
