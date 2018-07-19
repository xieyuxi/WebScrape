import urllib.request
from urllib import error

def download(url,user_agent = 'wswp' ,num_retries = 2):
    print('Downloading: '+ url)
    headers={'User-agent':user_agent}
    request=urllib.request.Request(url,headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except error.URLError as e:
        print('DownLoad Error:', e.reason)
        html = None
        if (num_retries > 0 ):
            if hasattr(e,'code') and 500 <= e.code <600:
                # recursively retry Sxx HTTP errors
                return download(url,num_retries - 1)
    return html
print(download('http://www.meetup.com'))

