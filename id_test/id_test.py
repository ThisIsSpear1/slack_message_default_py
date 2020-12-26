from slackbot import send_slack_message


class LoginError(Exception):
    def __init__(self, target_name):
        self.msg = '{target} 로그인 양식이 맞지 않습니다.'.format(target=target_name)
        send_slack_message(self.msg)

    def __str__(self):
        return self.msg


class DBError(Exception):
    def __init__(self, name, length, error):
        self.msg = '{name} 에 대한 {len} 행의 데이터 입력 작업 중 오류가 발생했습니다.\n{error}'\
            .format(name=name, error=error, len=length)
        send_slack_message(self.msg)

    def __str__(self):
        return self.msg
