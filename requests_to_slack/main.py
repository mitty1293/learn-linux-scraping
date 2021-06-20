import requests, json
import settings

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
    requests.post(settings.WEBHOOK_URL,
                data = json.dumps(
                    {
                        "blocks": [
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "Today's topic:\n*<http://www.usupi.org/sysad/294.html|Vol.294 - 共有ライブラリをざっくり理解する (レベル:中級)>*"
                                }
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "Previous:\n*<http://www.usupi.org/sysad/294.html|Vol.294 - 共有ライブラリをざっくり理解する (レベル:中級)>*"
                                }
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "Next:\n*<http://www.usupi.org/sysad/294.html|Vol.294 - 共有ライブラリをざっくり理解する (レベル:中級)>*"
                                }
                            }
                        ]
                    }
                ))

def main():
    return_rended_page()
    extract_urls()
    to_slack()

if __name__ == '__main__':
    main()