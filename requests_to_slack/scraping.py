from html import parser
import requests
from html.parser import HTMLParser

def return_rended_page():
    url = 'http://www.usupi.org/sysad/backno.html'
    rg = requests.get('http://splash:8050/render.html',
                    params={
                        'url': url,
                        'wait': 3
                    })
    print(rg.text)
    with open('rended.html', 'wb') as f:
        f.write(rg.content)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        return super().handle_starttag(tag, attrs)
    def handle_endtag(self, tag: str) -> None:
        return super().handle_endtag(tag)
    def handle_data(self, data: str) -> None:
        return super().handle_data(data)

def extract_urls():
    # render.htmlをbeautiful soupみたいな解析ツールで読み込んで該当URLを抽出する。
    parser = MyHTMLParser()
    