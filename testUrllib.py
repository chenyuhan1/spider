
# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, headers=headers, data=data, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# from urllib import request
# from urllib.parse import quote
#
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# }
# keyword = '壁纸'
# url = 'http://www.baidu.com/s?wd=' + quote(keyword)
# req = request.Request(url=url, headers=headers)
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome'
                  '/17.0.963.56Safari/535.11'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)