#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/03/06
# Created by FireEgret

from urllib import request, parse
import re

url = 'xxxxx/index.php'
req = request.Request(url)
req.add_header('Cookie','xxxxxx')

with request.urlopen(req) as f:
    data1 = f.read()
    res = data1.decode('utf-8')
    print(res)

    num = re.findall(re.compile(r'<br/>\s+(.*?)='), res)[0]
    post_data = parse.urlencode([
        ('v', eval(num))
    ])

    with request.urlopen(req, data=post_data.encode('utf-8')) as g:
        print(g.read().decode('utf-8'))

