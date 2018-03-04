from multiprocessing import Pool
from page_parsing import get_links_from
from link import channel_list


def get_all_links_from(channel):
    for num in range(1,57):
        get_links_from(channel, num)

if __name__ == '__main__':
    pool = Pool() #进程池
    pool.map(get_all_links_from, channel_list) #将所有频道链接放入函数，一次请求获取菜谱