import re
import requests
import lxml.html

def main():
    """
    メイン処理部
    :return: 
    """
    session = requests.Session() # for many pages.
    response = session.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)

        break # trial

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
    ebook = {
        'url': response.url,
        'title': root.cssselect('#bookTitle')[0].text_content(),
        'price': root.cssselect('.buy')[0].text.strip(),
        'content': [normalize_spaces(h3.text_content()) for h3 in root.cssselect('#content > h3')],
    }

    return ebook

def normalize_spaces(s):
    """
    連続する空白を１空白に置き換え、前後の空白を削除した文字列を取得
    :param s: string 
    :return: string
    """
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()