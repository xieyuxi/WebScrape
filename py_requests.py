'''
get()向服务器发送一个GET的请求，
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
'''