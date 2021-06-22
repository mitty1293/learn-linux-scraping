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
                                    "text": f"Today's topic:\n*<{topic_dict['todays']['url']}|{topic_dict['todays']['title']}>*"
                                }
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": f"Previous:\n*<{topic_dict['previous']['url']}|{topic_dict['previous']['title']}>*"
                                }
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": f"Next:\n*<{topic_dict['next']['url']}|{topic_dict['next']['title']}>*"
                                }
                            }
                        ]
                    }
                ))