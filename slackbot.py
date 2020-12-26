# Slackbot.py

from slacker import Slacker
from datetime import datetime
import in_token

token = in_token.eccess_token


def send_slack_message(msg, error=''):
    full_msg = msg
    if error:
        full_msg = msg + '\n에러 내용:\n' + str(error)
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
    slack = Slacker(token)
    #채널 이름 적기
    slack.chat.post_message('#test_bot_service', today + full_msg, as_user=True)


if __name__ == "__main__":
    # 일부러 에러가 발생하도록 함.
    try:
        a = 1/0
    except Exception as e:
        send_slack_message('테스트', e)
