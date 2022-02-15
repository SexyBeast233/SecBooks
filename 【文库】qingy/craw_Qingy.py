import time
from urllib.parse import unquote
from lxml import etree
from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import os
import time


def main():
    driver = webdriver.Chrome()
    WebDriverWait(driver, 10)
    driver.get('http://wiki.xypbk.com/')
    # 关键点！其实简单只在这里处理即可。
    # for cook in cookies:
    #     # 遍历删除sameSite,注意，旧版chrome可能是没有samesite
    #     try:
    #         cook.pop('sameSite')
    #     except:
    #         pass
    #     driver.add_cookie(cook)
    input("请手动登录后按Enter键继续")
    # 登录后刷新页面
    driver.refresh()
    # 将获取的html字符串转换为etree对象
    htmlObj = etree.HTML(driver.page_source)
    # 获取所有文件链接
    label_aList = htmlObj.xpath('//*[@class="file"]/a/@href')
    for url in label_aList:
        absFileName = ""
        try:
            pathList = url.split("/")
            absPath = os.getcwd()
            for indexNum in range(3, len(pathList)):
                if indexNum == len(pathList)-1:
                    absPath = os.path.join(absPath, pathList[indexNum].split(".md")[0]).replace(">", "").replace("<", "").strip(" ").replace("::", "").replace("*", "")
                    absFileName = os.path.join(absPath, pathList[indexNum]).replace(">", "").replace("<", "").strip(" ").replace("::", "").replace("*", "")
                else:
                    absPath = os.path.join(absPath, pathList[indexNum])
            if not os.path.isdir(absPath):
                os.makedirs(absPath)
        except Exception as e:
            #print(e)
            #print("[-]保存失败：{}".format(url))
            continue
        if not os.path.isfile(absFileName):
            print("[+]正在保存：{}".format(url))
            try:
                driver.get(url)
                htmlObj = etree.HTML(driver.page_source)  # 将获取的html字符串转换为etree对象
                texIinfo = htmlObj.xpath('//textarea/text()')[0].encode("utf-8")  # 获取文本内容
                # 获取图片链接列表
                imgList = htmlObj.xpath('//*[@id="render"]/p/img/@src')
                with open(absFileName, 'wb') as f:
                    f.write(texIinfo)
            except Exception as e:
                #print(e)
                print("[-]文件创建失败：{}".format(absFileName))
                continue
            for imgs in imgList:
                try:
                    if ":" in imgs:
                        continue
                    imgs = imgs.replace("./resource", "resource")
                    imgUrl = "http://wiki.xypbk.com/" + imgs
                    fileName = os.path.join(absPath, unquote(imgs).replace("/", "\\").lstrip("\\")).replace(">", "").replace("<", "").replace("::", "").replace("*", "")
                    filePath = "\\".join(fileName.split("\\")[:-1]).replace(">", "").replace("<", "").replace("::", "").replace("*", "")
                    if not os.path.isdir(filePath):
                        os.makedirs(filePath)
                    driver.get(imgUrl)
                    driver.save_screenshot(fileName)
                except Exception as e:
                    #print(e)
                    #print("[-]图片下载失败：{}".format(url))
                    os.remove(absFileName)
                    continue
    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    main()
