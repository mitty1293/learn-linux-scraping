from html import parser
import requests, random
from html.parser import HTMLParser

def return_rended_page(target_url, splash_api):
    rg = requests.get(splash_api,
                    params={
                        'url': target_url,
                        'wait': 10
                    })
    with open('rended.html', 'wb') as f:
        f.write(rg.content)
    # 完成後以下のprint文は消す
    print(rg.text)
    return rg.text

class MyHTMLParser(HTMLParser):
    # [0-9]{3}.html
    def __init__(self):
        super().__init__()
        self.backno = False
        self.backno_a = False
        self.backno_dict = {}
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h2" and "id" in attrs and attrs["id"] == "バックナンバー日付順":
            self.backno = True
        if self.backno and tag == "a":
            self.backno_a = True
    def handle_endtag(self, tag):
        if self.backno and tag == "ul":
            self.backno = False
    def handle_data(self, data):
        if self.backno_a:
            self.backno_dict[int(data[4:7])] = data
            self.backno_a = False

def extract_urls(rended_text):
    # render.htmlをbeautiful soupみたいな解析ツールで読み込んで該当URLを抽出する。
    parser = MyHTMLParser()
    parser.feed(rended_text)
    parser.close()
    # 完成後以下のprint文は消す
    print(len(parser.backno_dict))
    # 以下はpost_to_slackメソッドに移す
    volno, title = random.choice(list(parser.backno_dict.items()))
    # 完成後以下のprint文は消す
    print(str(volno) + "," + title)
    return parser.backno_dict