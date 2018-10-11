import requests
from PIL import Image
from io import BytesIO

url = 'http://www.baidu.com'
r = requests.get(url)
r.encoding = 'utf-8'
print(r.text)
print(r.status_code)
print(r.headers)
print('Date:', r.headers.get('Date'))
print(r.encoding)
print(r.cookies)

'''
# 传递参数：不如http://aaa.com?pageId=1&type=content
params = {'k1': 'v1', 'k2': ['v2', 2, 'v3']}
r = requests.get('http://httpbin.org/get', params)
print(r.url)
'''

'''
# 二进制数据
r = requests.get('https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2316242837,3672164063&fm=27&gp=0.jpg')
images = Image.open(BytesIO(r.content))
images.save('images/meinv.jpg')
'''

'''
# json处理
r = requests.get('http://github.com/timeline.json')
print(type(r.json))
print(r.text)
'''
'''
# 原始数据的处理
r = requests.get('http://www.test.com/test.jpg')
with open('test.jpg', 'wb+') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)
'''
'''
# 提交表单
form = {'username': 'user', 'password': 'pass'}
r = requests.post('http://httpbin.org/post', data=form)
print(r.text)
'''
'''
# cookie
url = 'http://www.baidu.com'
r = requests.get(url)
cookies = r.cookies
for k, v in cookies.get_dict().items():
    print(k, v)

cookies = {'c1': 'v1', 'c2': 'v2'}
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r)
print(r.text)
'''
'''
# 重定向和重定向历史
r = requests.head('http://github.com', allow_redirects=True)
print(r.url)
print(r.status_code)
print(r.history)
'''

# # 代理
# proxies = {'http': ',,,', 'http': '...'}
# r = requests.get('...', proxies=proxies)
