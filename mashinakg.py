import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open ('data.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([data['title'], data['image'], data['price'], data['description']])

def get_html(url):
    response = requests.get(url)
    # print(response)
    return response.text

url = 'https://www.mashina.kg/search/all/'

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find('div', class_ = 'table-view-list image-view clr label-view').find_all('div', class_ = 'list-item list-label')
    for product in products:
        title = product.find('div',class_ = 'block title').text
        # image = 'https://im.mashina.kg/tachka/images/' + product.find('img').get('src')
        price = product.find('div', class_ = 'block price').text
        description = product.find('div',class_ = 'block info-wrapper item-info-wrapper').text.strip()
        dict_ = {'title': title, 'image': image, 'price': price, 'description': description}
        write_to_csv(dict_)

with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title                   ', 'image                  ', 'price                  ', 'description                   '])

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('ul', class_ = 'pagination').find_all('li')
    # print(page_list)
    last_page = page_list[-1].text
    # print(last_page)
    return int(last_page)

get_total_pages(get_html(url))

def main():
    url = 'https://www.mashina.kg/search/all/'
    pages = '?page='
    html = get_html(url)
    number = get_total_pages(html)
    get_data(html)
    for i in range(2, number + 1):
        url_with_page = url + pages + str(i)
        # print(url_with_page)
        html = get_html(url_with_page)
        get_data(html)

main()
