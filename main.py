from script import *
from bs4 import BeautifulSoup
import requests
import time
import csv


def get_url(url):
    r = requests.get(url, headers=headers, timeout=5)
    if r.ok:  # status code 200
        return r
    else:
        print('Ошибка доступа к сайту:', r.status_code)


def write_csv(data):
    with open('olx.csv', 'a', newline='') as f:
        order = ['title', 'link', 'phone']
        writer = csv.DictWriter(f, delimiter=';', fieldnames=order)
        writer.writerow(data)


def get_html(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    ads = soup.find_all('h3', attrs={'class': 'lheight22 margintop5'})

    for i in ads:
        title = i.find('strong').text
        link = i.find('a').get('href')
        driver.get(link)

        try:
            cookie_close = driver.find_element_by_xpath('//*[@id="cookiesBar"]/button')
            cookie_close.click()
        except:
            pass

        try:
            phone_btn = driver.find_element_by_xpath('//*[@id="contact_methods"]/li[2]/div/span')
            phone_btn.click()
            time.sleep(2)
            phone = driver.find_element_by_xpath('//*[@id="contact_methods"]/li[2]/div/strong/span[1]').text
        except:
            pass

        data = {'title': title, 'link': link, 'phone': phone}
        write_csv(data)


def main():
    input_url = input('Введите ссылку для парсинга: ')
    print('Пример ссылки для парсинга: https://www.olx.ua/nedvizhimost/')

    pagination = input('Укажите количество страниц для парсинга: ')
    pagination = int(pagination.strip())
    print('Парсинг начался...')

    for i in range(1, 1 + pagination):
        url = f'{input_url}?page={i}'
        html = get_url(url)
        page = get_html(html)


if __name__ == '__main__':
    main()
