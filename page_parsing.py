import requests
from bs4 import BeautifulSoup
import time
import pymongo

#链接数据库，创建表
client = pymongo.MongoClient('localhost', 27017)
meishij = client['meishij']
url_list = meishij['page_url']

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

#抓取每一页所有菜谱
def get_links_from(channel, pages):
    #http://www.meishij.net/china-food/caixi/qingzhencai/?&page=2
    list_view = '{}?&page={}'.format(channel, str(pages))
    wb_data = requests.get(list_view, headers = header)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # print(soup.find('div',class_='searchform_div')('input')[0]['placeholder'])
    if soup.find('div',class_='searchform_div'):
        try:
            nav = soup.find('div',class_='searchform_div')('input')[0]['placeholder']
        except:
            nav = None
    else:
        pass

    if soup.find('div', class_='i_w'):
        for link in soup.select('.listtyle1'):
            try:
                item_link = link.select('a')[0]['href'] #获取链接
            except:
                item_link = None
            try:
                title = link.select('.c1')[0]('strong')[0].text #获取标题
            except:
                title = None
            try:
                comment = link.select('.c1')[0]('span')[0].text.split()[0] #获取评论数
            except:
                comment = '0'
            try:
                likes = link.select('.c1')[0]('span')[0].text.split()[-2] #获取人气数
            except:
                likes = '0'
            try:
                #加判断，去除不规则格式的老文章
                if comment.isdigit() and likes.isdigit():
                    url_list.insert_one({'url':item_link, 'title':title, 'comment':int(comment),\
                                         'likes':int(likes), 'series':nav}) #保存到MongoDB
                else:
                    pass
            except:
                print('数据出错')
            try:
                print({'url':item_link, 'title':title, 'comment':int(comment),\
                                         'likes':int(likes), 'series':nav})
            except:
                print('标题出错')
    else:
        pass

# get_links_from('http://www.meishij.net/chufang/diy/jiangchangcaipu/?&page=', 1)

