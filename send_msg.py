import requests
def send_msg(msg):
    # 企业微信机器人 key
    key = 'a4e3adxx-xxx8-xxxx-bxxx-7dab753def76'
    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('key',key ),
    )

    data = '{{ "msgtype": "text", "text": {{ "content": "{msg}" }} }}'.format(msg=msg)

    print(data)
    response = requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send', headers=headers, params=params,
                             data=data.encode('utf-8'))
    if response.json()['errcode']==0:
        return True
    else:
        return False


if __name__ == '__main__':
    send_msg('hello')
