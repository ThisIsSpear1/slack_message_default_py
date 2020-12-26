from slackbot import send_slack_message

name_list = []


def crawl_something(name):
    return


for name in name_list:
    try:
        crawl_something(name)
    except:
        send_slack_message('크롤링 중 {name} 를 처리하는 데 오류가 발생했습니다.'.format(name=name))
