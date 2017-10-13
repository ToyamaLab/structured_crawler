import requests
import lxml.html

response = requests.get('https://hogehoge.tk/webdev/color/')
root = lxml.html.fromstring(response.content)
root.make_links_absolute(response.url)

print("test")

for a in root.cssselect('body > div.container-fluid > table > tbody > tr > td:nth-child(1) > table > tbody > tr'):
    print a
    color_name = a.cssselect('td:nth-child(2)').text
    print(color_name)

