#!/usr/bin/env python

import urllib2
import csv
import random
import time

url = 'http://mis.tse.com.tw/data/TSEIndex.csv?r=%s' % random.randrange(1,10000)
stock_list = ['0050', '3227']

page = urllib2.urlopen(url)
reader = csv.reader(page)
tse_index = []
for row in reader:
    tse_index.append({'no':row[0], 'time':row[1], 'value':row[2], 'range':row[3]})
print('Content-Type: text/plain')
print(tse_index[1]['time'], tse_index[1]['value'], tse_index[1]['range'])
for no in stock_list:
    page = urllib2.urlopen('http://mis.tse.com.tw/data/%s.csv?r=%s' % (no, random.randrange(1,10000)))
    reader = csv.reader(page)
    for row in reader:
        print(row[2], row[0], row[8], row[1])
