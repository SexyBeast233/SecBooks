# Jupyter Notebook 未授权访问远程命令执行漏洞

## 漏洞描述

Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。

如果管理员未为Jupyter Notebook配置密码，将导致未授权访问漏洞，游客可在其中创建一个console并执行任意Python代码和命令。

## 漏洞影响

> [!NOTE]
>
> Jupyter Notebook

## FOFA

> [!NOTE]
>
> app="Jupyter-Notebook" && body="Terminal"

## 漏洞复现

访问目标, 点击 Terminal 打开命令行界面

![](http://wikioss.peiqi.tech/vuln/ju-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

执行命令并反弹shell

![](http://wikioss.peiqi.tech/vuln/ju-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)