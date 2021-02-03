import os
import urllib.request
import sys
from threading import Thread
import time
import socket
url_file = 'urls.text'

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)


#new = open('200.txt','w',encoding='UTF-8',newline='')
#with open(url_file, "r", encoding='utf-8',) as f:
#f = ["http://yunlsp.com","http://www.yunlsp.com","https://yunlsp.com","https://www.yunlsp.com","https://baidu.com","http://baidu.com"]
#new = open('200.txt','w',encoding='UTF-8',newline='')
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36')]


# 定义异步函数
def async(func):
    def wrapper(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

import re
import subprocess


def tracertIP(ip,count,status,dict,u):
    p = subprocess.Popen(['tracert',ip],stdout=subprocess.PIPE)
    text = ''
    while True:
        line = p.stdout.readline()
        if not line:
            break
        #print(type(line))
        text += (line.decode('gbk','ignore'))
    dict[u] =  "正常访问{}次,状态码{},追踪信息：{}".format(count,status,text)
    #print(dict)
   # print(1,dict)
    return dict

#@async
def test_url():
    urlsuccesdict = {}
    urlfailddict = {}
    success = 0
    faild = 0
    with open(PROJECT_PATH + '/test_domain/urls/urls', "r", encoding='utf-8',) as f:
        for line in f:
            #u =('http://'+line).strip('\n')
            u = ( line).strip('\n')
            try :
                test = opener.open(u)
                #print(test.__dict__)
                #print(test.status)

                urlsuccesdict[u] = "正常访问{}次,状态码{},追踪信息：{}".format(success++1,test.status,"")
                urlsuccesdict = tracertIP('118.25.86.211',success++1,test.status,urlsuccesdict,u)
               # print(1)
                #print(u+"正常")
                #new.write(u+'\n')
            except  :

                urlfailddict[u] = "失败访问{}次,追踪信息：{}".format(faild++1,"")
               # text = tracertIP('118.25.86.211')
                urlfailddict =  tracertIP('118.25.86.211',faild++1,"400",urlsuccesdict,u)
                print(2)
                #print(urlfailddict)
        print(2,urlsuccesdict,"\n",urlfailddict)




if __name__ == '__main__':
    while True:
        #time.sleep(1)
        test_url()
    #tracertIP('www.yunlsp.com')
#tracertIP('baidu.com')






# grep -v -e 172.17.0.10 -e 172.17.0.11 -e 172.17.0.13 -e 172.17.0.15  -e 172.17.0.16 -e 172.17.0.17 -e 172.17.0.2 -e 172.17.0.30 -e 172.17.0.34 -e 172.17.0.4 -e 172.17.0.5  -e 172.17.0.6 -e 172.17.0.7 -e 172.17.0.9 -e 172.17.112.10 -e 172.17.112.6 -e 172.17.16.100 -e 172.17.16.102 -e 172.17.16.105 -e 172.17.16.108 -e 172.17.16.117 -e 172.17.16.118 -e 172.17.16.120 -e 172.17.16.122 -e 172.17.16.123 -e 172.17.16.124 -e 172.17.16.128 -e 172.17.16.130 -e 172.17.16.131 -e 172.17.16.132 -e 172.17.16.142 -e 172.17.16.15 -e 172.17.16.18 -e 172.17.16.2 -e 172.17.16.20 -e 172.17.16.23 -e 172.17.16.25 -e 172.17.16.26 -e 172.17.16.28 -e 172.17.16.29 -e 172.17.16.3 -e 172.17.16.30 -e 172.17.16.31 -e 172.17.16.32 -e 172.17.16.33 -e 172.17.16.35 -e 172.17.16.36 -e 172.17.16.37 -e 172.17.16.38 -e 172.17.16.39 -e 172.17.16.4 -e 172.17.16.40 -e 172.17.16.41 -e 172.17.16.42 -e 172.17.16.43 -e 172.17.16.45 -e 172.17.16.47 -e 172.17.16.48 -e 172.17.16.49 -e 172.17.16.5 -e 172.17.16.54 -e 172.17.16.57 -e 172.17.16.58 -e 172.17.16.6 -e 172.17.16.65 -e 172.17.16.67 -e 172.17.16.68 -e 172.17.16.7 -e 172.17.16.71 -e 172.17.16.72 -e 172.17.16.74 -e 172.17.16.76 -e 172.17.16.77 -e 172.17.16.78 -e 172.17.16.79 -e 172.17.16.83 -e 172.17.16.88  -e 172.17.16.9 -e 172.17.16.95 -e 172.17.16.97 -e 172.17.32.11 -e 172.17.32.4 -e 172.17.64.11 -e 172.17.80.20 -e 172.17.80.21 -e 172.17.80.3 -e 172.17.96.3 -e 172.17.96.4 -e 172.17.96.5





