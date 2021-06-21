import requests, json
import settings
import scraping

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
    scraping.return_rended_page()
    scraping.extract_urls()
    to_slack()

if __name__ == '__main__':
    main()