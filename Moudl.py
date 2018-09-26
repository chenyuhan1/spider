# _*_ coding: utf-8 _*_
import urllib.request
import re
import pymysql


class Sql(object):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='18279438873',
        db='noveltest',
        charset='utf8'
    )

    def addnovel(self, sort, sortname, name,imgurl,
                 description, status, author):
        cur = self.conn.cursor()
        cur.execute("insert into novel(sort, sortname, name,imgurl, description" +
                      ",status,author) values(%s, '%s', '%s', '%s', '%s', '%s', '%s')"
                    % (sort, sortname, name, imgurl, description, status, author))
        lastrowid = cur.lastrowid
        cur.close()
        self.conn.commit()
        return lastrowid

    def addchapter(self, novelid, title, content):
        cur = self.conn.cursor()
        cur.execute("insert into chapter(novelid, title, content) values(%s,"
                    "'%s', '%s')" % (novelid, title, content))
        cur.close()
        self.conn.commit()


mysql = Sql()
sort_dict = {
    1: '玄幻魔法',
    2: '武侠修真',
    3: '纯爱耽美',
    4: '都市言情',
    5: '职场校园',
    6: '穿越重生',
    7: '历史军事',
    8: '网游动漫',
    9: '恐怖灵异',
    10: '科幻小说',
    11: '美文名著'
}


# def getChaptercontent(url, url_html, lastrowid, title):
#     html = urllib.request.urlopen('%s/%s' % (url, url_html)).read().decode('gbk').encode('utf-8')
#     html = html.decode('utf-8')
#     reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
#     html = re.findall(reg, html, re.S)[0]
#     mysql.addchapter(lastrowid, title, html)

# def getchapterList(url, lastrowid):
#     html = urllib.request.urlopen(url).read().decode('gbk').encode('utf-8')
#     html = html.decode('utf-8')
#     reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
#     chapterInfo = re.findall(reg, html)
#     for url_html, title in chapterInfo:
#         getChaptercontent(url, url_html, lastrowid, title)

def getNovel(url, sort_id, sort_name):
    html = urllib.request.urlopen(url).read().decode("gbk").encode('utf-8')
    html = html.decode('utf-8')
    reg = r'<meta property="og:novel:book_name" content="(.*?)"/>'
    bookname = re.findall(reg, html)[0]
    reg = r'<meta property="og:description" content="(.*?)"/>'
    description = re.findall(reg, html, re.S)[0]
    reg = r'<meta property="og:image" content="(.*?)"/>'
    image = re.findall(reg, html)[0]
    reg =  r'<meta property="og:novel:author" content="(.*?)"/>'
    author = re.findall(reg, html)[0]
    reg = r'<meta property="og:novel:status" content="(.*?)"/>'
    status = re.findall(reg, html)[0]
    reg = r'<a href="(.*?)" class="reader"'
    chapterUrl = re.findall(reg, html)[0]
    print(sort_id, sort_name, bookname, image, description, status, author)
    lastrowid = mysql.addnovel(sort_id, sort_name, bookname, image, description, status, author)
    #  getchapterList(chapterUrl, lastrowid)


def getList(sort_id, sort_name):
    html = urllib.request.urlopen('http://www.quanshuwang.com/list/%s_1.html'
                                  % sort_id).read().decode('gbk').encode('utf-8')
    reg = r'<a target="_blank" href="(.*?)" class="l mr10">'
    html = html.decode('utf-8')
    urlList = re.findall(reg, html)
    for url in urlList:
        getNovel(url, sort_id, sort_name)


for sort_id, sort_name in sort_dict.items():
    print("正在获取数据")
    getList(sort_id, sort_name)