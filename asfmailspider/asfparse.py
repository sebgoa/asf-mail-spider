#!/usr/bin/env python
# encoding: utf-8
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import datetime
from prettytable import PrettyTable as pt
import json	
import urllib, os

#site = urllib.urlopen(link)
#meta = site.info()
#print "Content-Length:", meta.getheaders("Content-Length")[0]


def main():
	
    URL = "http://mail-archives.apache.org/mod_mbox/"
	
    try:
        fh=open('items.json')
    except:
        print "Generate items.json file first"

    foobar=json.loads(fh.read())	

    for item in foobar:
        if 'project' in item.keys():
            print item['project'][0].upper()
            for list in item['list']:
                print list

        if 'ml' in item.keys():
            x = pt(["Date","# Messages"," URL ", " Size"])
            print item['ml']
            for dt in item['datatime']:
                date = dt[0].split(' ')[0]
                url_mbox = URL + item['ml'] + date.split('-')[0] + date.split('-')[1] + ".mbox"
                ml_open = urllib.urlopen(url_mbox)
                meta = ml_open.info()
                ml_size = meta.getheaders("Content-Length")[0]
                x.add_row([date,dt[1], url_mbox, ml_size])
            print x

if __name__ == '__main__':
	main()

