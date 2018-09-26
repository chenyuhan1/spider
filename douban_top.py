import requests
from lxml import etree
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='18279438873',
    db='douban',
    charset='utf8'
)


def add_douban(name, rating):
    cur = conn.cursor()
    cur.execute("insert into douban_top(name, rating) values('%s', '%s')" % (name, rating))
    cur.close()
    conn.commit()


x = 0
s = requests.session()
for i in range(0, 300, 25):
    url = 'https://movie.douban.com/top250/?start-' + str(id)
    r = requests.get(url)
    r.encoding = 'utf-8'
    root = etree.HTML(r.content)
    items = root.xpath('//ol/li/div[@class="item"]')
    # print(len(items))
    for item in items:
        title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
        name = title[0].encode('gb2312', 'ignore').decode('gb2312')
        rating = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
        x += 1
        add_douban(name, rating)