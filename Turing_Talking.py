import sys
import json
import time
import requests

'''
人机对话所用机器人为图灵机器人，每日总请求数为100，请手动去图灵官网 www.tuling123.com 申请自己的机器人替换配置 KEY 与 USER_ID
已替换 帐号 xiong8024591314@126.com 15728005468
'''
# Tuling Config
Tuling_API_URL = "http://openapi.tuling123.com/openapi/api/v2"

# 替换 API_KEY 如开密匙就填密匙
Tuling_API_KEY = "8fe25964da1a49299607ddddd60688e6"

# 替换 UserId
Tuling_USER_ID = "438679"
name = ""


class colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


def ask_tuling(msg):
    tuling_post_data = {"reqType": 0, "perception": {"inputText": {"text": msg}}, "userInfo": {
        "apiKey": Tuling_API_KEY,
            "userId": Tuling_USER_ID
    }}
    json_data = json.dumps(tuling_post_data).encode('utf8')
    resp = requests.post(url=Tuling_API_URL, headers={'content-type': 'application/json'}, data=json_data)
    if resp.status_code == 200:
        r = resp.json()
        if r:
            return r["results"][0]["values"]["text"]


def human_ai_mode():
    print(colors.PINK + "煎饼：Hi~我是煎饼呀~" + colors.END)
    while True:
        q = input(colors.BLUE + name + "：" + colors.END)
        if q == "exit":
            sys.exit(0)
        a = ask_tuling(q)
        time.sleep(1)
        print(colors.PINK + "煎饼：{}".format(a) + colors.END)


if __name__ == "__main__":
    print("提示：示例程序所选用的机器人每日有次数限额，可自行申请替换，具体请参考代码注释")
    time.sleep(1)
    print("提示：输入" + colors.RED + "exit" + colors.END + "可退出聊天")
    name = input(colors.YELLOW + "请输入你的名字：" + colors.END)
    if name == "":
        name = "你"
    time.sleep(1)
    print(colors.GREEN + "正在进入呼叫煎饼...." + colors.END)
    time.sleep(1)
    print(colors.GREEN + "连接成功！" + colors.END)
    time.sleep(1)
    human_ai_mode()
