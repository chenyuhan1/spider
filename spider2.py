# _*_ coding:utf-8 _*_
import urllib
import urllib.request
import re


def getUrlList():

    req = urllib.request.Request('http://www.budejie.com/video/')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) '
                                 'AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13')
    res = urllib.request.urlopen(req)
    html = res.read()
    html = html.decode("utf-8")
    reg = r'data-mp4="(.*?)">'
    urlList = re.findall(reg, html)
    for url in urlList:
        urllib.urlretrieve(url, 'mp4/%s.mp4' % url.split('/')[-1])


# for page in range(0, 2):
#     getUrlList(page+1)
getUrlList()