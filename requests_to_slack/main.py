import requests

def return_rended_page():
    url = 'http://www.usupi.org/sysad/backno.html'
    rg = requests.get('http://splash:8050/render.html',
                    params={
                        'url': url,
                        'wait': 3
                    }
    )
    print(rg.text)
    with open('rended.html', 'wb') as f:
        f.write(rg.content)

def extract_urls():
    # render.htmlをbeautiful soupみたいな解析ツールで読み込んで該当URLを抽出する。
    pass

def to_slack():
    # slackへ通知する
    pass

def main():
    return_rended_page()
    extract_urls()
    to_slack()

if __name__ == '__main__':
    main()