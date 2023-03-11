
import requests
from bs4 import BeautifulSoup

new_list = []
news_url_list = []
def parse():
    url = 'https://kaktus.media/?lable=8&date=2023-03-10&order=time'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    news1 = soup.find('div', 
    class_ = 'Tag--articles').find_all('div', 
    class_ = 'Tag--article')
    
    global new_list, news_url_list
    sum_ = 0
    for news_ in news1:
        news_url = soup.find('div', 
        class_ = 'Tag--articles').find('a', 
        class_ = 'ArticleItem--name').get('href')
        news_url_list.append(news_url)
        head = news_.find('a', class_ = 'ArticleItem--name').text
        sum_ = sum_ + 1
        new_list.append(f'{sum_}. {head}')
    # print(new_list)
    print(news_url_list)
parse()