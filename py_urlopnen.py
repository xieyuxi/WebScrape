'''
1.urlopen的使用源码：
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile=None, capath=None, cadefault=False, context=None):
其中重要参数：
url：可以是请求的链接，也可以是请求(Request)的对象；
data: 请求中附加送给服务器的数据(如：用户名和密码等);
timeout：超时的时间，以秒为单位，超过多长时间即报错/;

最基础的用法 -- urlopen(url, data=None) 
'''
import urllib.request
import urllib.parse
import socket
import urllib.error 

# a.仅有URL的情况，data = none:
res1 = urllib.request.urlopen('http://www.baidu.com')
# 请求返回的对象类型为HTTPResponse对象，主要包含read()、status、getheader(name)等 
# print(type(res1))  -- 返回的对象   <class 'http.client.HTTPResponse'> 
# print(res1.status) -- 返回的状态   200
# print(res1.read()) -- 返回的网页内容

# b.data不为空的情况(模拟了表单提交的方式，以 POST 方式传输数据):
# 如果要添加该参数，并且如果它是字节流编码格式的内容，即 bytes 类型,则需要通过 bytes()方法转化。
# 如果传递了这个参数，则它的请求方式就不再是 GET方式，而 是 POST 方式。
# bytes() 将字符串转换为字节流，后面是编码规则'utf-8'
# urlencode（）将一个字段或元组转换为url查询字符串
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding ='utf-8') 
# 这里注意URL后面跟的post
res2 = urllib.request.urlopen('http://httpbin.org/post', data=data) 
print(res2) # 这里返回的是一个HTTPResponse object
# print(res2.read())

# c.TimeOut:
# 用于设置超时时间，单位为秒。如果请求超出了设置的这个时间,还没有得 到响应,就会抛出异常。
try: 
    res3 = urllib.request.urlopen('http://httpbin.org/get ',timeout=0.1) 
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
