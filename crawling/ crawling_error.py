import slackbot


# 여기에서 크롤링 진행
def run():
    return


if __name__ == "__main__":
    try:
        run()
        slackbot.send_slack_message('크롤링이 완료되었습니다.')
    except Exception as e:
        slackbot.send_slack_message('크롤링 작업 중 오류가 발생했습니다!', e)