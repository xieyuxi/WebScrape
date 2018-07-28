# requests.get()方法：
'''
get()向服务器发送一个GET的请求，这里可以理解为向服务器发送了一个包含了各种信息的Request对象，
def get(url, params=None, **kwargs)，其中重要的参数有：
1、url: 具体的URL请求地址；
2、params: (可选) 字典或者字节流，通过请求一起传送；
3、**kwargs：其他可能需要增加的额外数据
4、返回一个requests.Response对象。

# 仅有URL参数
import requests 
r = requests.get('https://www .baidu.com/') 
print(type(r)) 
print(r.status_code) 
print (type(r.text)) 
print(r.text) 
print(r.cookies)


# 有URL和params参数
import requests 
data = {'name':'xieyuxi', 'age': 22}
r = requests.get('http://httpbin.org/get', params=data) 
#print(r.text) 
# 这里网站返回的是Json格式的string,如果要直接解析放回结构得到一个字典，可以直接调用json()方法：
print(type(r)) #<class 'requests.models.Response'>
print(r.json())
print(type(r.json()))
print(isinstance(r.json(),dict))

# 有URL和headers参数：
import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
r = requests.get('https://www.zhihu.com/explore', headers=headers) 
pattern = re.compile('xplore-feed.*?question_link.*?>(.*?)</a>', re.S) 
titles = re.findall(pattern, r.text) 
print(str(titles).replace('\\n',''))


# 下载图片并保存
import requests
r = requests.get('https://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(r.content)
'''

# requests.post()方法：
'''
def post(url, data=None, json=None, **kwargs):
向服务器发送POST请求，这里可以理解为向服务器发送了一个包含了各种信息的Request对象：
1、url: 具体的URL请求地址；
2、data: (可选) 字典（会被编码）、字节流或者类似文件的对象，都会被打包进Request对象；
3、**kwargs：其他可能需要增加进Request对象的额外数据
4、返回一个requests.Response对象。    

import requests 
data = {'name':'xieyuxi', 'age': 22}
r = requests.post('http://httpbin.org/post', params=data) 
print(r.text)


# 文件的上传
import requests 
files = {'file':open('favicon.ico','rb')} 
r = requests.post('http://httpbin.org/post', files=files) 
print(r.text) 


# 由于Http协议是无状态的，即浏览完网站后关闭浏览器链接断开，下次要访问要重连。
# 也就导致服务器无法分辨是谁浏览了网页。为了维持用户在网站的状态，比如登陆、购物车等，出现了先后出现了四种技术，分别是隐藏表单域、URL重写、cookie、session。
# 神奇的Cookie：
# 我们经常会在登录网站时选择30天内记住我，或者自动登录选项，这正是cookie的作用之一
# Cookie是由HTTP服务器设置的，保存在浏览器中，但HTTP协议是一种无状态协议，在数据交换完毕后，服务器端和客户端的链接就会关闭，每次交换数据都需要建立新的链接。
# 举个恰当的例子cookie就像是会员卡，保存了我们的信息，下次去银行办理业务，银行可以根据这个会员卡查询到我们的信息，进而获取到更多的'服务'。
# 这里我们登录知乎之后打开并把请求的Cookie记录下来，通过模拟请求，可以达到成功登录的效果。
import requests 

headers = {
    'Cookie' : 'cookie: d_c0="AKBgutCuiw2PTuM1x50hpkB78pxZa3j2tkQ=|1525492258"; _zap=f79d0745-0690-4dca-a5ad-274b503823a0; __utmz=155987696.1525503382.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=155987696.1367069581.1525503382.1525503382.1525705414.2; tgw_l7_route=53d8274aa4a304c1aeff9b999b2aaa0a; _xsrf=ba638e94-b7ba-4cef-97cf-ee0a0a8c49fe; q_c1=26f5ef5f642046b99e753be0dedd3fe8|1532747297000|1525492260000; capsion_ticket="2|1:0|10:1532747299|14:capsion_ticket|44:MzA0MmY2NjA2MTRhNDIyZDkwMzQ5ODFmMDUxYjY1YzQ=|b522736122849a864edd56ceef73c3e43cbad8eb358a1c29578531f771760a6e"; l_n_c=1; r_cap_id="OGNkNGFjN2NjMjhiNDY3YzhkMmZmZDMwMzkyYjM0NDY=|1532747301|a834f7f4b8e34c470d061552bfbb709b148fb46a"; cap_id="NGUxNGM5ZGQxNWFkNGYyZmJmOTE2MGM4OTZhOGUyYmQ=|1532747301|51aac3dcf680b6af5922ab978d9fea26562479ab"; l_cap_id="Mzg4MDc1ZTk2NTJhNGJjMWJjNjBiMTk3YTFjZjYyMTg=|1532747301|a8a3c3c761865b7788681bdf6d4aee7ac6cfc615"; n_c=1; z_c0=Mi4xMXVSeEFRQUFBQUFBb0dDNjBLNkxEUmNBQUFCaEFsVk5OeXhKWEFDZ1VuVHFTM2NoTDdVNkYwQksyelBFd25PeG1R|1532747319|cb13b28da1203f2d8f69ddfc795816999af86a58',
    'Host' : 'www.zhihu.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers = headers) 
print(r.cookies) # 这里可以看到是一个<RequestsCookieJar>对象
for key,value in r.cookies.items():
    print(key + '=' + value + '\n')
print(r.text)


# 维持同一个会话的Session：
# session的作用和cookie差不多，也是用来解决Http协议不能维持状态的问题。
# 但是session只存储在服务器端的，不会在网络中进行传输，所以较cookie来说，session相对安全一些。
# 但是session是依赖cookie的，当用户访问某一站点时，服务器会为这个用户产生唯一的session_id,并把这个sessookie的形式发ion_id以c送到客户端，
# 以后的客户端的所有请求都会自动携带这个cookie（前提是浏览器支持并且没有禁用cookie）。


# 这里我们请求了一个测试网址:'http://httpbin.org/cookies/set/number/123456789',
# 请求这个网址时，可以设置一个 cookie，名称叫作 number，内容是 123456789，
# 随后又请求了 http://httpbin.org/cookies, 可以获取当前的 Cookies。

import requests 
requests.get('http://httpbin.org/cookies/set/number/123456789') 
r = requests.get('http://httpbin.org/cookies') 
print(r. text) # "cookies":{}   并没有成功获取到Cookie

import requests 
s = requests.Session() 
# s.request()的用法:
#     def request(self, method, url,
#           params=None, data=None, headers=None, cookies=None, files=None,
#           auth=None, timeout=None, allow_redirects=True, proxies=None,
#           hooks=None, stream=None, verify=None, cert=None, json=None):
# s.get()的用法：
#    def get(self, url, **kwargs):
s.get('http://httpbin.org/cookies/set/number/123456789') 
r = s.get('http://httpbin.org/cookies') 
print(r.text) 

# SSL证书的验证：
# 这里我们以12306为例
import requests 
# response = requests.get('https://www.12306.cn') 
# print(response.status_code) # requests.exceptions.SSLError: HTTPSConnectionPool(host='www.12306.cn', port=443):
# 如果我们不想进行验证是否可行
response = requests.get('https://www.12306.cn', verify=False) 
print(response.status_code) # 请求成功，但是会有一个'Adding certificate verification is strongly advised'的警告
# 那么我们就用证书的方式进行请求(以下仅为演示代码)：
# 我们需要有 crt 和 key 文件，并且指定它们的路径。
# 注意，本地私有证书的 key 必须是解密状态，加密状态的 key 是不支持的。
response = requests .get('https://www.12306.cn', cert=('/path/server.crt','/path/key')) 
print(response.status_code)

# 代理设置：
# 对于某些网站，在测试的时候请求几次， 能正常获取内容。 
# 但是一旦开始大规模爬取，对于大规 模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，
# 更甚者可能会直接封禁客户端 的 IP，导致一定时间段内无法访问。
# 为了解决这个问题，我们需要用到 proxies 参数设置代理。
import requests 
proxies = {
    'http':'http: I 110 .10.1.10: 3128', 
    'https':'http: //10.10.1.10: 1080',
}
# 若代理需要使用 HTTP Basic Auth，可以使用类似 http://user:password@host:port
# proxies = {'http':'http://user:password@10.10.1.10:3128/',}
requests.get('httpsd://www.taobao. com', proxies=proxies) 

# 超时设置：
# 为了防止服务器不能及时响应，应该设置一个超时时间， 即超过了这个时间还没有得到响应，那就报错。 
# 这需要用到 timeout 参数,以秒为单位。直接不加或time = none表示永久等待
import requests 
r = requests.get('https:www.taobao.com',timeout = 1)
print(r.status_code) 

# 身份认证：
# 法1：我们需要引入HTTPBasicAuth类，即将HTTP的认证信息附加入Request请求对象中
import requests 
from requests.auth import HTTPBasicAuth 
r = requests.get('http://localhost:sooo', auth=HTTPBasicAuth('username','password')) 
# 发2：
# 传入一个HTTPBasicAuth类如果麻烦，可以直接传一个元组，它会默认使用 HTTPBasicAuth 这个类来认证。
# r = requests.get('http://localhost:sooo', auth=('username','password')) 
print (r.status_code) 
# 如果用户名和密码正确的话，请求时就会自动认证成功，会返回 200 状态码；如果认证失败， 则 返回 401 状态码。

# Prepared Request:
# 我们首先引入prepare_request的概念，提前先组装一个PreparedRequest对象用于发送和接受请求
# 然后用url,data和headers参数构造了一个Request对象，
# 调用Session的Prepare_Request()方法将其转换成一个Prepare_Request对象，然后调用send（）方法发送即可。
# 可以看到的是我们同样达到了POST的请求效果。

from requests import Request, Session 
url = 'http://httpbin.org/post'
data = {'name':'germey'} 
headers = {'User-Agent':'Mozilla/s.o (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53 .0.2785.116 Safari/537.36'} 
s = Session() 
req = Request('POST', url, data=data, headers=headers) 
prepped = s.prepare_request(req) 
r = s.send(prepped) 
print(r. text) 

