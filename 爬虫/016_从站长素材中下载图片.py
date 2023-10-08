"""
第一页 https://sc.chinaz.com/tupian/kejijiaotongtupian.html
第二页 https://sc.chinaz.com/tupian/kejijiaotongtupian_2.html
请求方法:GET
"""
import urllib.request
from lxml import etree

def create_request(page):
    base_url = 'https://sc.chinaz.com/tupian/kejijiaotongtupian_'
    if page==1:
        url = 'https://sc.chinaz.com/tupian/kejijiaotongtupian.html'
    else:
        url = base_url+str(page)+".html"
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "cz_statistics_visitor=b11821cc-8961-d0fd-8b1a-df3112a636f2; Hm_lvt_ca96c3507ee04e182fb6d097cb2a1a4c=1695192073; toolbox_urls=imu.edu.cn|qq.com; Hm_lvt_aecc9715b0f5d5f7f34fba48a3c511d6=1694875588,1695192044,1696141365; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1695202962,1696419368; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1696419619",
        "Host": "sc.chinaz.com",
        "Referer": "https://sc.chinaz.com/tupian/kejijiaotongtupian.html",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(content):
    # 下载图片
    # urllib.request.urlretrieve('图片地址','文件的名字')
    tree = etree.HTML(content)
    name_list = tree.xpath("//div[@class='item']/img/@alt")
    src_list = tree.xpath("//div[@class='item']/img/@data-original")
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = "https:"+src
        urllib.request.urlretrieve(url=url,filename='./img/'+name + '.jpg')


if __name__ == '__main__':
    start_page = int(input("请输入起始页码:"))
    end_page = int(input("请输入结束页码:"))
    for page in range(start_page,end_page+1):
        # 定制请求
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 从网页中获取我们想要的数据
        download(content)