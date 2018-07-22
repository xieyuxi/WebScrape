'''
1.Request的使用源码：
def __init__(self, url, data=None, headers={},origin_req_host=None,unverifiable=False,method=None):
这里和urlopen比较一下差异：
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile=None, capath=None, cadefault=False, context=None):
虽然两者都是向服务器发出请求，但是Request显然增加了headers等参数。

其中重要参数：
headers：是一个字典，它就是请求头，添加请求头最常用的用法就是通过修改 User-Agent 来伪装成浏览器。
origin_req_host: 指的是请求方的 host名称或者 IP 地址。 
method：是一个字符串，用来指示请求使用的方法，比如 GET、 POST 和 PUT。
'''
from urllib import request, parse

url = 'http://www.baidu.com/post'
# 注意这里的headers是一个字典
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
   'host': 'www.baidu.com'
}
# 这里我们会设置一个data传入请求
dict = {
    'name' : 'Germey',
    'password': '123321'
}
# 这里如果直接编码是会报错，TypeError: not a valid non-string sequence or mapping object
# （错误的）data = parse.urlencode('dict');
data = bytes(parse.urlencode(dict),'utf8')
# 因为传入请求的data需要转换成字节流，所以我们用bytes（）和parse的urlencode方法将dict从字符串转换为字节流
req = request.Request(url = url,data=data,headers = headers,method = 'POST')
# headers 也可以用 add_header()方法来添加: req.addheaders('User-Agent p,’Mozilla/4 .0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8')) 
