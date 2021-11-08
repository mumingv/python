#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: main.py
          Desc: 
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-12-27 23:47:59
       History:
 ***********************************************************/
'''

import fileinput
import requests
import urllib
import sys

error_count = 0

INPUT_ENCODEING = 'utf8'
OUTPUT_ENCODEING = 'utf8'

'''
python debug.py input_file_utf8
'''

input_file = sys.argv[1]
out_file = open('res_%s' % input_file, 'w')
error_file = open('error_%s' % input_file, 'w')

data = {}
data['us_ip_port'] = '10.206.225.34:8211'

data['client'] = 'test'
data['os'] = 'android'
data['version'] = '8.1.0'
data['environment'] = 'define'
data['longtitude'] = '116.280523'
data['latitude'] = '40.051242'
data['query_type'] = 1
data['service'] = ''
data['hint_id'] = ''
data['username'] = 'xxx'

url = 'http://123.56.21.232:8254/myprojects/demo/get_tts_news/index.php'

for raw_line in fileinput.input(sys.argv[1]):
    line = raw_line.strip()
    if INPUT_ENCODEING != OUTPUT_ENCODEING:
        line = line.decode(INPUT_ENCODEING).encode(OUTPUT_ENCODEING).strip();

    data['query'] = line
    source_type = 'other'
    source_sub_type = 'other'

    try:
        obj = requests.post(url, data).json()
        if 'content' in obj and len(obj['content']) > 0:
            res_item = obj['content'][0]
            if 'source_type' in res_item:
                source_type = res_item['source_type']
            if 'source_sub_type' in res_item:
                source_sub_type = res_item['source_sub_type']
    except:
        error_count += 1
        print '%s:[%d]' % (input_file, error_count)
        error_file.write(raw_line)
        error_file.flush()

    out_file.write(data['query'])
    out_file.write('\t')
    out_file.write(source_type)
    out_file.write('\t')
    out_file.write(source_sub_type)
    out_file.write('\n')
    out_file.flush()
