from html import parser
import requests
from html.parser import HTMLParser

def return_rended_page(target_url, splash_api):
    rg = requests.get(splash_api,
                    params={
                        'url': target_url,
                        'wait': 5
                    })
    with open('rended.html', 'wb') as f:
        f.write(rg.content)
    # 完成後以下のprint文は消す
    print(rg.text)
    return rg.text

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
#         return super().handle_starttag(tag, attrs)
#     def handle_endtag(self, tag: str) -> None:
#         return super().handle_endtag(tag)
#     def handle_data(self, data: str) -> None:
#         return super().handle_data(data)

def extract_urls(rended_text):
    # render.htmlをbeautiful soupみたいな解析ツールで読み込んで該当URLを抽出する。
    # parser = MyHTMLParser()
    pass
