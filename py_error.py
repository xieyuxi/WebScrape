'''
URLError是urllib.error模块的一个类，当使用request产生异常时都可以通过捕获这个类来处理。
它具有一个属性reason，返回错误的原因。
另外，它还有一个子类是HTTPError，专门处理 HTTP 请求错误。它有如下 3 个属性：
 1）code： 返回 HTTP 状态码，比如 404 表示网页不存在， 500 表示服务器内部错误等。
 2）reason：同父类一样，用于返回错误的原因。 
 3）headers： 返回请求头。
'''

from urllib import request, error 
import socket 

try:
    response = request.urlopen('https://xieyuxi.com/index.htm') 
    #response = request.urlopen('https://www.baidu.com', timeout = 0.01) 

except error.HTTPError as e: 
    print(e.reason, e.code, e.headers, sep='\n') 
except error.URLError as e: 
    print(e.reason) 
# 当然有时reason返回的也有可能是一个对象,这里reason中返回的是socket.timeout 类。
    if isinstance(e.reason,socket.timeout): 
        print('TIME OUT') 
else: 
    print('Request Successfully') 
