"""
作业一：

安装并使用 requests、bs4 库
爬取猫眼电影的前 10 个电影名称、电影类型和上映时间
并以 UTF-8 字符集保存到 csv 格式的文件中
"""
import random
import requests
import pandas
from bs4 import BeautifulSoup

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

user_agent = random.choice(user_agents)
cookie = "uuid=50E6A800CF2311EA989D8534BBE132DA05FF834B02AA48A2A2AB4E8059A790A7"
header = {'user-agent': user_agent, 'CooKie': cookie}  # 必须要有cookie

def get_repsonse_text():
    """
    获取 response.text
    """
    url = 'https://maoyan.com/films?showType=3'
    response = requests.get(url, headers=header)
    return response.text

def get_split_2nd_item(text):
    return text.strip().split(':')[1].strip()

def e01():
    """
    1. 从主页面就能获取到前10个电影
    2. 电影名称、类型和上映时间也能从主页面获取，不需要做模拟链接点击操作
    """
    movies_count = 10
    
    rsp_text = get_repsonse_text()
    bs_info = BeautifulSoup(rsp_text, 'html.parser') 
    output = []
    for tags in bs_info.find_all('dl', attrs={'class': 'movie-list'}):
        for dd_tag in tags.find_all('dd', limit=movies_count):   
            t_div = dd_tag.find('div', attrs={'class': 'channel-detail movie-item-title'})
            movie_title = t_div.find('a').text.strip()
            # print(movie_title)
            type_div = dd_tag.find_all('div', attrs={'class': 'movie-hover-title'})[1]
            movie_type = get_split_2nd_item(type_div.text)
            # print(movie_type)
            date_div = dd_tag.find('div', attrs={'class': 'movie-hover-title movie-hover-brief'})
            plan_date = get_split_2nd_item(date_div.text)
            # print(plan_date)
            output.append([movie_title, movie_type, plan_date])

    # 存储到 csv 文件
    movie = pandas.DataFrame(data=output)
    movie.to_csv('./top10movies.csv', encoding='utf-8', index=False, header=False)


if __name__ == '__main__':
    e01()  
