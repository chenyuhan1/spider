import time
from selenium import webdriver

browser = webdriver.Chrome('D:\Chromedriver\chromedriver.exe')
browser.set_page_load_timeout(50)

# 有多少页商品
browser.get('http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3')
page_info = browser.find_element_by_css_selector(
    'body > div.wrap > div.search_container > div.pagem.product_list_pager > div')
# 共 40 页，每页 60 条
pages = int((page_info.text.split(', ')[0]).split(' ')[1])
print('商品有%d页' % pages)
for page in range(pages):
    if page > 2:
        break
    print('第%d页' % (page+1))
    url = 'http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3&page=%d' + str(page + 1)
    browser.get(url)
    browser.execute_script("windows.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    goods = browser.find_element_by_css_selector(
        'body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')
    print('%d页有%d件商品' % ((page + 1), len(goods)))
    for good in goods:
        try:
            title = good.find_element_by_css_selector('a:nth-child(1)').text
            price = good.find_element_by_css_selector('div>a>span').text
            print(title, price)
        except:
            print(good.text)