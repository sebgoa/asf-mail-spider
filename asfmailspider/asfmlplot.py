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
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json	
	
def main():
	
    try:
        fh=open('items.json')
    except:
        print "Generate items.json file"
    foobar=json.loads(fh.read())	
    
    fig = plt.figure(1)
    ax=fig.add_subplot(111)

    for f in foobar:
        if 'ml' in f.keys():
           print f['ml']
           count=[]
           datapoint=[]
           for d in f['datatime']:
               datapoint.append(datetime.datetime.strptime(str(d[0]),'%Y-%m-%d %H:%M:%S'))
               count.append(int(d[1]))
           p=ax.plot(datapoint,count,label=f['ml'])  
   
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%y'))
    fig.autofmt_xdate()
    plt.title('Mail Messages')
    plt.legend(loc=2)
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
	main()

