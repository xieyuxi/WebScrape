'''
Handler：解决各种问题的处理器，针对不同的问题有不同的handler，而这些handlers的父类是一个名为'BaseHandler'的类，在urllib.request 模块里
OpenerDirector：另一个urllib.request中较重要的类。以下是对OpenerDirector的定义：
  The OpenerDirector manages a collection of Handler objects that do all the actual work. 
  The OpenerDirector is a composite object that invokes the Handlers needed to open the requested URL.
可以看出OpenerDirector是管理各种handlers来干具体活的，并且调用了需要打卡请求链接的handlers。
我们之前用的urlopen（）这个方法，实际上它就是 urllib 为我们提供的一个 Opener，而opener实际是OpenerDirector的一个实例。

个人对OpenerDirector和handlers的理解是：
OpenerDirector好比是一个‘人'，而各种handlers好比是创造好要解决问题的工具
handler这个工具造好了，但不会自己去解决问题，那怎么办呢？
那么我们的OpenerDirector就出场了，但是OpenerDirector这个‘人'是个宽泛的抽象概念
那么我们就给他做一个实例(opener)，比如：‘张三'，张三是‘人'这个抽象概念的实例，那么由张三亲自使用我们的handlers去解决问题
'''

# 1.HTTPBasicAuthHandler 验证handler
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener 
from urllib.error import URLError 

username = 'username' 
password ='password' 
url = 'http://localhost:sooo/' 
p = HTTPPasswordMgrWithDefaultRealm() 
# 利用 add_password（）添加进去用户名和密码
p.add_password(None,url,username,password) 
# 实例化 HTTPBasicAuthHandler对象，其参数是HTTPPasswordMgrWithDefaultRealm 对象
auth_handler = HTTPBasicAuthHandler(p) 
# 为auth_handler这个工具造一个使用者（opener）出来
opener = build_opener(auth_handler) 
try: 
    # 这里可以想象为使用者（opener）拿着工具（auth_handler）来打开我们的层层布防的大门（url）
    result = opener.open(url) 
    html = result. read().decode('utf 8') 
    print(html) 
except URLError as e: 
    print(e.reason) 

# 2.ProxyHandler 代理handler
# 在真实IP访问服务器间设置代理服务器，伪装IP而不会被因为访问频率过高而遭封杀
from urllib.error 
import URLError 
from urllib.request import ProxyHandler, build_opener 
proxy_handler = ProxyHandler({'http':'http://127.o.o.1:9743','https':'https://127.0.0.1:9743'}) 
opener = build_opener(proxy_handler) 
try: 
    response = opener.open('https://www.baidu.com') 
    print(response.read().decode('utf-8')) 
except URLError as e: 
    print(e.reason) 

# 3.HTTPCookieProcessor Cookie handler
# Cookies 指某些网站为了辨别用户身份、 进行会话跟踪而存储在用户本地终端上的数据。
import http.cookiejar, urllib.request 
cookie = http.cookiejar.CookieJar() 
handler = urllib.request.HTTPCookieProcessor(cookie) 
opener = urllib.request.build_opener(handler) 
response = opener. open ('http://www.baidu.com') 
for item in cookie: 
    print(item.name + " = " + item.value)
