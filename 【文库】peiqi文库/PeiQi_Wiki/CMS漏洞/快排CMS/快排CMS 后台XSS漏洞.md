# 快排CMS 后台XSS漏洞

## 漏洞描述

快排CMS 后台存在XSS漏洞，通过后台构造特殊语句可以造成访问网站的用户被XSS影响

## 漏洞影响

> [!NOTE]
>
> 快排 CMS <= 1.2

## 环境搭建

https://gitee.com/qingzhanwang/kpcms

## 漏洞复现

漏洞出现在登录后台的网站编辑的位置，由于没有对输出的字符进行过滤，导致XSS

![](http://wikioss.peiqi.tech/vuln/kp-8.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

主页版权处嵌入XSS代码

![](http://wikioss.peiqi.tech/vuln/kp-10.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

![](http://wikioss.peiqi.tech/vuln/kp-9.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

