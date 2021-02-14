import os
from slack_sdk.webhook import WebhookClient
from typing import List, Any

slackWebHookUrl = os.environ["SLACK_WEB_HOOK_URL"]

class SlackData:
    def __init__(self, url: str, price: str) -> None:
        self.url = url
        self.price = price

def buildSection(data: List[SlackData]) -> List[Any]:
    output = []
    for d in data:
        output.append({
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"{d.url} {d.price}"
			}
        })

    return output

        # {
		# 	"type": "divider"
		# },
		

def sendWebHook(fallbackMsg: str, data: List[SlackData]) -> None:
    blocks = buildSection(data)

    webhook = WebhookClient(slackWebHookUrl)

    response = webhook.send(text=fallbackMsg, blocks=blocks)
    assert response.status_code == 200
    assert response.body == "ok"