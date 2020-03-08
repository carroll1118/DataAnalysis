import requests
from lxml import etree
import time
url = "https://movie.douban.com/subject/30413052/comments?start=%d&limit=20&sort=new_score&status=P"
#请求头创建
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'ll="118110"; bid=WOtRzZzB5n0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1582074463%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1948976768.1582074463.1582074463.1582074463.1; __utmc=30149280; __utmz=30149280.1582074463.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1954541914.1582074463.1582074463.1582074463.1; __utmb=223695111.0.10.1582074463; __utmc=223695111; __utmz=223695111.1582074463.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=fZlVZoEw3nfJ2LTBimMXwbQ3rZSTg4gt; __utmt=1; __utmb=30149280.1.10.1582074463; __gads=ID=c96f4a66287780c3:T=1582074474:S=ALNI_MZg6jl7uY5UK19V5rQcW3J0oTvm6Q; ct=y; _pk_id.100001.4cf6=7c86c6587c0eeadf.1582074463.1.1582074503.1582074463.',
'Host':'movie.douban.com',
'Referer':'https://movie.douban.com/subject/30413052/reviews?start=20',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
if __name__ == '__main__':
    fp = open('./climb.csv',mode='w',encoding='utf-8')
    fp.write('author\tcomment\tvote\n')
    for i in range(26):
        if i == 25:
            url_climb = url%(490)
        else:
            url_climb = url%(i*20)
        response = requests.get(url_climb,headers=headers)
        response.encoding = 'utf-8'
        text = response.text
        html = etree.HTML(text)
        comments = html.xpath('//div[@id="comments"]/div[@class="comment-item"]')
        for comment in comments:
            #作者
            author = comment.xpath('./div[@class="avatar"]/a/@title')[0].strip()
            #评论
            p = comment.xpath('.//span[@class="short"]/text()')[0].strip()
            #赞同
            vote = comment.xpath('.//span[@class="votes"]/text()')[0].strip()
            fp.write('%s\t%s\t%s\n'%(author,p,vote))
        print('第%d页保存成功'%(i+1))
        time.sleep(1)
    fp.close()
