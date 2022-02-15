# Wayos AC集中管理系统默认弱口令  CNVD-2021-00876

## 漏洞描述

深圳维盟科技股份有限公司是国内领先的网络设备及智能家居产品解决方案供应商，主营产品包括无线网关、交换机、国外VPN、双频吸顶ap等。

AC集中管理平台存在弱口令漏洞，攻击者可利用该漏洞获取敏感信息。

## 漏洞影响

> [!NOTE]
>
> AC集中管理系统

## FOFA

> [!NOTE]
>
> title="AC集中管理系统"

## 漏洞复现

默认弱口令为 admin:admin

![](http://wikioss.peiqi.tech/vuln/wayos-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

![](http://wikioss.peiqi.tech/vuln/wayos-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

> [!NOTE]
>
> 已上传 https://github.com/PeiQi0/PeiQi-WIKI-POC Goby & POC 目录中
>
> Wayos_AC_Centralized_management_system_Default_weak_password

![](http://wikioss.peiqi.tech/vuln/wayos-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)