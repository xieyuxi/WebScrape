'''
一、项目需求：
1、要提取出猫眼电影 TOPlOO 的电影名称、时间、评分、图片等信息；
2、提取站点为：http://maoyan.com/board/4；
3、提取的结果以文件的形式保存下来。

二、网站分析：
1、榜单排名规则分析：将猫眼电影库中的经典影片，按照评分和评分人数从高到低综合排序取前100名。这一部分排名
2、URL分析：
    a. 我们要爬取得是前100的电影，而每一页只有10部电影，也就是我们全部爬完需要先找出前十页URL的规律
    b.直接点击第一页最下面的第 2 页，我们看到URL发生了变化，增加了一个偏移量变量“?offset=10”，电影此时显示的是第10-20部；
    c.再试了一下加入将偏移量设置为“?offset=20”,则显示的是20-30部的电影；
    d.不难得出偏移量的值是当页第一部电影的排序号；
    e.但我们怎么处理第一页呢？其实http://maoyan.com/board/4 的偏移量可以设置为“?offset=0”就可以显示第一页的电影。
    （那如果“?offset=2”将如何显示呢？自己可以动手试一下）
    经过测试我们可以得出偏移量实际代表了电影起始的位置，比如“?offset=10”是指电影从10开始显示，并且每页显示10部电影；
3、爬取数据的分析：
    以下是我们截取的html部分含有我们所需要的元素的片段：
<dd>
    <i class="board-index board-index-1">1</i>
    <a title="霸王别姬" class="image-link" href="/films/1203" data-act="boarditem-click" data-val="{movieId:1203}">
        <img class="poster-default" alt="" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
        <img class="board-img" alt="霸王别姬" src="http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
        <div class="board-item-content">
            <div class="movie-item-info">
                <p class="name"><a title="霸王别姬" href="/films/1203" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
                <p class="star"> 主演：张国荣,张丰毅,巩俐 </p>
                <p class="releasetime">上映时间：1993-01-01(中国香港)</p>    
            </div>
            <div class="movie-item-number score-num">
            <p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
            </div>
        </div>
    </div>
</dd>
    很明显一部电影信息对应的源代码是一个dd节点，我们用正则表达式来提取这里面的一些电影信息。
    注意：括号的用途是表明需要匹配出的字符串，并把匹配的字符串分为一个组，后面方面拆分统计
    a.排名信息：排名信息是在 class 为 board-index的 i 节点内:
        <dd>.*?board-index.*?>(.*?)</i> 
    b.电影的图片：注意这里有一个小技巧，规避其他相对位置的图片，即在匹配图片链接时，加个http:
        <dd>.*?.*?src="(http:.*?)"
    c.电影的名称：这里需要注意的是title名称的双引号
        <dd>.*?title="(.*?)"
    d.电影的主演：这里需要注意的是匹配后的演员名单中有空格，需要用strip()方法去空格
        <dd>.*?"star">(.*?)</p>
    e.电影的上映时间和上映地：
        <dd>.*?"releasetime">(.*?)</p>
    f.电影的评分：
        <dd>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>

'''
import requests
import re

myheader = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
movie = []
f = open("movie.txt","a")
for i in range(0,101,10):
    url = 'http://maoyan.com/board/4?offset=' + str(i)
    response = requests.get(url,headers = myheader)
# print(response) # 这里我们获得了response的一个对象<Response [200]>
# print(response.text) # 这里我们才得到真正的HTML
    html = response.text
# print(html)
# 参数re.S表示“.”的作用扩展到整个字符串，包括“\n”。
# pattern_rank  = re.compile('<dd>.*?board-index.*?>(.*?)</i>',re.S) # 这里我们可以获取到电影的排名信息
# pattern_pic   = re.compile('<dd>.*?src="(http:.*?)"',re.S)         # 这里我们可以获取到电影的图片
# pattern_name  = re.compile('<dd>.*?title="(.*?)"',re.S)            # 这里我们可以获取到电影的名字
# pattern_cast  = re.compile('<dd>.*?"star">(.*?)</p>',re.S)         # 这里我们可以获取到电影的演员表
# pattern_time  = re.compile('<dd>.*?"releasetime">(.*?)</p>',re.S)  # 这里我们可以获取到电影的上映时间
# pattern_score = re.compile('<dd>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?<dd>', re.S) # 这里我们可以获取到电影的评分

# 注意其中的括号是将匹配的内容分为一个组(.*?)，这样不同信息就在不同组
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?src="(http:.*?)".*?title="(.*?)".*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>',re.S)
    items = re.findall(pattern,html)
    
    for item in items:
        dic = {
            '排名'     :item[0],
            '片名'     :item[2],
            '主演'     :item[3].strip()[3:],
            '上映时间' :item[4].strip()[5:],
            '评分'     :item[5]+item[6],
            '图片'     :item[1]
        }
        movie.append(dic)
        f.write(str(dic)+'\n')

f.close(
    
)
'''
import json
import requests
from requests.exceptions import RequestException
import re
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?src="(http:.*?)".*?title="(.*?)".*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        # print(item[0])
        # print(item[1])
        # print(item[2])
        # print(item[3].strip()[3:])
        # print(item[4])
        # print(item[5]+item[6])

        # yield {
        #     'index': item[0],
        #     'image': item[1],
        #     'title': item[2],
        #     'actor': item[3].strip()[3:],
        #     'time': item[4].strip()[5:],
        #     'score': item[5] + item[6]
        # }
        dic = {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
        movie.append(dic)
        print(movie)


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
'''