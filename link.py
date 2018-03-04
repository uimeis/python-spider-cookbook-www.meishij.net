import requests
from bs4 import BeautifulSoup
import pymongo
import time

url = 'http://www.meishij.net/shicai/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

#获取5大类链接
def get_head_urls(url):
    res = requests.get(url, headers = header)
    soup = BeautifulSoup(res.text, 'lxml')
    link = soup.select('.listnav_ul > li > a')
    for i in link:
        i = 'http://www.meishij.net' + str(i.get('href'))
        print(i)

# get_head_urls(url)

#5大类链接列表
head_list = '''
    http://www.meishij.net/chufang/diy/
    http://www.meishij.net/china-food/caixi/
    http://www.meishij.net/china-food/xiaochi/
    http://www.meishij.net/chufang/diy/guowaicaipu1/
    http://www.meishij.net/hongpei/
'''

#获取所有类目链接
def get_total_urls(head_urls):
    res = requests.get(head_urls, headers = header)
    soup = BeautifulSoup(res.text, 'lxml')
    link = soup.select('.listnav_dl_style1 > dd > a')
    for i in link:
        url = i.get('href')
        name = i.text
        print({'url':url,'name':name})

# for i in head_list.split():
#     total_url = get_total_urls(i)
#     print(total_url)

#全部链接
total_url = '''{'url': 'http://www.meishij.net/chufang/diy/jiangchangcaipu/', 'name': '家常菜'}
{'url': 'http://www.meishij.net/chufang/diy/sijiacai/', 'name': '私家菜'}
{'url': 'http://www.meishij.net/chufang/diy/langcaipu/', 'name': '凉菜'}
{'url': 'http://www.meishij.net/chufang/diy/haixian/', 'name': '海鲜'}
{'url': 'http://www.meishij.net/chufang/diy/recaipu/', 'name': '热菜'}
{'url': 'http://www.meishij.net/chufang/diy/tangbaocaipu/', 'name': '汤粥'}
{'url': 'http://www.meishij.net/chufang/diy/sushi/', 'name': '素食'}
{'url': 'http://www.meishij.net/chufang/diy/jiangliaozhanliao/', 'name': '酱料蘸料'}
{'url': 'http://www.meishij.net/chufang/diy/weibolucaipu/', 'name': '微波炉'}
{'url': 'http://www.meishij.net/chufang/diy/huoguo/', 'name': '火锅底料'}
{'url': 'http://www.meishij.net/chufang/diy/tianpindianxin/', 'name': '甜品点心'}
{'url': 'http://www.meishij.net/chufang/diy/gaodianxiaochi/', 'name': '糕点主食'}
{'url': 'http://www.meishij.net/chufang/diy/ganguo/', 'name': '干果制作'}
{'url': 'http://www.meishij.net/chufang/diy/rujiangcai/', 'name': '卤酱'}
{'url': 'http://www.meishij.net/chufang/diy/yinpin/', 'name': '时尚饮品'}
{'url': 'http://www.meishij.net/chufang/diy/zaocan/', 'name': '早餐'}
{'url': 'http://www.meishij.net/chufang/diy/wucan/', 'name': '午餐'}
{'url': 'http://www.meishij.net/chufang/diy/wancan/', 'name': '晚餐'}
{'url': 'http://www.meishij.net/chufang/diy/xiawucha/', 'name': '下午茶'}
{'url': 'http://www.meishij.net/chufang/diy/yexiao/', 'name': '夜宵'}
{'url': 'http://www.meishij.net/chufang/diy/laonian/', 'name': '老年人'}
{'url': 'http://www.meishij.net/chufang/diy/chanfu/', 'name': '产妇'}
{'url': 'http://www.meishij.net/chufang/diy/yunfu/', 'name': '孕妇'}
{'url': 'http://www.meishij.net/chufang/diy/baobaocaipu/', 'name': '宝宝食谱-婴儿食谱'}
{'url': 'http://www.meishij.net/china-food/caixi/chuancai/', 'name': '川菜'}
{'url': 'http://www.meishij.net/china-food/caixi/xiangcai/', 'name': '湘菜'}
{'url': 'http://www.meishij.net/china-food/caixi/yuecai/', 'name': '粤菜'}
{'url': 'http://www.meishij.net/china-food/caixi/dongbeicai/', 'name': '东北菜'}
{'url': 'http://www.meishij.net/china-food/caixi/lucai/', 'name': '鲁菜'}
{'url': 'http://www.meishij.net/china-food/caixi/zhecai/', 'name': '浙菜'}
{'url': 'http://www.meishij.net/china-food/caixi/sucai/', 'name': '苏菜'}
{'url': 'http://www.meishij.net/china-food/caixi/qingzhencai/', 'name': '清真菜'}
{'url': 'http://www.meishij.net/china-food/caixi/mincai/', 'name': '闽菜'}
{'url': 'http://www.meishij.net/china-food/caixi/hucai/', 'name': '沪菜'}
{'url': 'http://www.meishij.net/china-food/caixi/jingcai/', 'name': '京菜'}
{'url': 'http://www.meishij.net/china-food/caixi/hubeicai/', 'name': '湖北菜'}
{'url': 'http://www.meishij.net/china-food/caixi/huicai/', 'name': '徽菜'}
{'url': 'http://www.meishij.net/china-food/caixi/yucai/', 'name': '豫菜'}
{'url': 'http://www.meishij.net/china-food/caixi/xibeicai/', 'name': '西北菜'}
{'url': 'http://www.meishij.net/china-food/caixi/yuguicai/', 'name': '云贵菜'}
{'url': 'http://www.meishij.net/china-food/caixi/jiangxicai/', 'name': '江西菜'}
{'url': 'http://www.meishij.net/china-food/caixi/shancicai/', 'name': '山西菜'}
{'url': 'http://www.meishij.net/china-food/caixi/guangxicai/', 'name': '广西菜'}
{'url': 'http://www.meishij.net/china-food/caixi/gangtai/', 'name': '港台菜'}
{'url': 'http://www.meishij.net/china-food/caixi/other/', 'name': '其它菜'}
{'url': 'http://www.meishij.net/china-food/xiaochi/sichuan/', 'name': '四川小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/guangdong/', 'name': '广东小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/beijing/', 'name': '北京小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/shanxii/', 'name': '陕西小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/shandong/', 'name': '山东小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/shanxi/', 'name': '山西小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/hunan/', 'name': '湖南小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/henan/', 'name': '河南小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/shanghai/', 'name': '上海小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/jiangsu/', 'name': '江苏小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/hubei/', 'name': '湖北小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/chongqing/', 'name': '重庆小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/tianjin/', 'name': '天津小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/hebei/', 'name': '河北小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/zhejiang/', 'name': '浙江小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/xinjiang/', 'name': '新疆小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/jiangxi/', 'name': '江西小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/fujian/', 'name': '福建小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/guangxi/', 'name': '广西小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/yunnan/', 'name': '云南小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/liaoning/', 'name': '辽宁小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/jilin/', 'name': '吉林小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/guizhou/', 'name': '贵州小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/anhui/', 'name': '安徽小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/taiwan/', 'name': '台湾小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/gansu/', 'name': '甘肃小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/xianggang/', 'name': '香港小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/menggu/', 'name': '蒙古小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/ningxia/', 'name': '宁夏小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/qinghai/', 'name': '青海小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/hainan/', 'name': '海南小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/xizang/', 'name': '西藏小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/chengduxiaochi/', 'name': '成都小吃'}
{'url': 'http://www.meishij.net/china-food/xiaochi/heilongjiang/', 'name': '黑龙江小吃'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/hanguo/', 'name': '韩国料理'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/japan/', 'name': '日本料理'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/ccmd/', 'name': '西餐面点'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/faguo/', 'name': '法国菜'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/yidali/', 'name': '意大利餐'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/usa/', 'name': '美国家常菜'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/dongnanya/', 'name': '东南亚菜'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/moxige/', 'name': '墨西哥菜'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/aozhou/', 'name': '澳大利亚菜'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/other/', 'name': '其他国家'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/canqianxiaochi/', 'name': '餐前小吃'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/tangpin/', 'name': '汤品'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/zhucai/', 'name': '主菜'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/zhushi/', 'name': '主食'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/yinpin/', 'name': '饮品'}
{'url': 'http://www.meishij.net/chufang/diy/guowaicaipu1/tiandian/', 'name': '甜点'}
{'url': 'http://www.meishij.net/hongpei/dangaomianbao/', 'name': '蛋糕面包'}
{'url': 'http://www.meishij.net/hongpei/bingganpeifang/', 'name': '饼干配方'}
{'url': 'http://www.meishij.net/hongpei/tianpindianxin/', 'name': '甜品点心'}
{'url': 'http://www.meishij.net/hongpei/hongpeigongju/', 'name': '烘焙工具'}
{'url': 'http://www.meishij.net/hongpei/hongpeichangshi/', 'name': '烘焙常识'}
{'url': 'http://www.meishij.net/hongpei/hongpeiyuanliao/', 'name': '烘焙原料'}'''

#链接数据库
client = pymongo.MongoClient('localhost', 27017) #链接数据库
meishij = client['meishij'] #建立数据库名称
sheet_tab = meishij['class_url'] #数据库表的名称

# #保存到MongoDB
# a = total_url.split('\n')
# print(len(a))
# for i in a:
#     s = eval(i)
#     print(type(s))
#     sheet_tab.insert_one(s)

#查询数据库
channel_list = []
for channel in sheet_tab.find():
    channel_list.append(channel['url'])

# print(len(channel_list))