import requests
import re
import html5lib
from bs4 import BeautifulSoup

s = requests.session()
url_login = 'http://accounts.douban.com/login'
url_contacts = "http://www.douban.com/people/****/contacts"
