import requests, json
import settings

def post_to_slack(**topic_dict):
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