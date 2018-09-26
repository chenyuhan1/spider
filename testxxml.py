from lxml import etree
import requests

req = requests.get('http://www.jxufe.edu.cn/')
req.encoding = 'utf-8'
text = req.text
html = etree.HTML(text)
result = html.xpath('//div[@class="headRightTop"]/ul[1]/li/a/text()')
print(result)

