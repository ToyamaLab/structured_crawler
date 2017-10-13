import time
import re

import requests
import lxml.html
from pymongo import MongoClient

def main():
    """
    メイン処理部
    :return: None
    """

    client = MongoClient('localhost', 27017)
    collection = client.scraping.ebooks
    collection.create_index('key', unique=True)

    response = requests.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        key = extract_key(url)
        ebook = collection.find_one({'key': key})

        if not ebook:
            time.sleep(1)
            response = requests.get(url)
            ebook = scrape_detail_page(response)
            if ebook is not None:
                collection.insert_one(ebook)
                print(ebook)


def scrape_list_page(response):
    """
    一覧ページのResponseから詳細ページのURLをジェネレート
    :param response: 
    :return: url
    """
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#listBook a[itemprop="url"]'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    """
    詳細ページのResponseから電子書籍の情報をdictで返す。
    :param response: 
    :return: dict 
    """

    root = lxml.html.fromstring(response.content)
    try:
        ebook = {
            'url': response.url,
            'key': extract_key(response.url),
            'title': root.cssselect('#bookTitle')[0].text_content(),
            'price': root.cssselect('.buy')[0].text.strip(),
            'content': [normalize_spaces(h3.text_content()) for h3 in root.cssselect('#content > h3')],
        }
    except IndexError:
        ebook = None

    return ebook

def extract_key(url):
    """
    url文字列からキーとして末尾のISBNを取り出す。
    :param url: string
    :return: string
    """
    m = re.search(r'/([^/]+)$', url).group(1)
    return m


def normalize_spaces(s):
    """
    連続する空白を１空白に置き換え、前後の空白を削除した文字列を取得
    :param s: string 
    :return: string
    """
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()