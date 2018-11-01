import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 '
                  'Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)'
}
response = requests.get('https://m.toutiao.com/i6618526058113155597/', headers=headers)
print(response.status_code)
print(response.text)