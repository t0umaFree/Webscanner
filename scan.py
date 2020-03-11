import requests
import threading
import re

def scan(urls):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Connection':'keep - alive',
        'Accept': 'application / json, text / javascript, * / *; q = 0.01'
            }
    data = {'url':urls,'location_capcha':'no'}
    test = requests.post(url='http://whatweb.bugscaner.com/what.go',headers=headers,data=data)
    json2 = test.json()
    print(json2)
    print('---------------')

    print('url:{}'.format(json2['url']))
    print('网页状态:{}'.format(json2['status_code']))
    print('IP:{}'.format(json2['ip']))
    print('地址:{}'.format(json2['address']))
    print('JS框架:{}'.format(json2['JavaScript Frameworks']))
    print('CMS:{}'.format(json2['CMS']))
    print('Web Server:{}'.format(json2['Web Servers']))
    print('网页语言:{}'.format(json2['Programming Languages']))
    print('CDN:{}'.format(json2['CDN']))
    print('网络存储地址:{}'.format(['Network Storage']))
    print('-------------')

scan(input('URL'))
