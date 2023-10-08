# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=40&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=60&limit=20

# page    1  2   3   4
# start   0  20  40  60

# start （page - 1）*20


# 下载豆瓣电影前10页的数据
# （1） 请求对象的定制
# （2） 获取响应的数据
# （3） 下载数据
import urllib.parse
import urllib.request


def create_request(page):
    # 因为这是get请求，请求的参数都在URL中，所以先考虑封装URL的条件
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    # 因为是get请求，所以不需要进行二次编码，post请求是需要进行二次编码的
    data = urllib.parse.urlencode(data)
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    url = base_url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        # 这必须加cookie,不加cookie真不行啦
        'cookie': 'BIDUPSID=20B48AA69066FECFB975482140CC6C45; PSTM=1692975106; BAIDUID=20B48AA69066FECF934B15B17EDBCE81:FG=1; BD_UPN=12314753; H_WISE_SIDS=110085_268592_259642_256151_269832_269904_270604_271035_271022_271171_271177_267659_271323_270102_271562_271188_272223_272279_272008_272455_269729_271689_272821_273094_273161_273121_273301_270055_273704_273734_274177_269610_273917_274234_273043_272806_272560_272802_188331; H_WISE_SIDS_BFESS=110085_268592_259642_256151_269832_269904_270604_271035_271022_271171_271177_267659_271323_270102_271562_271188_272223_272279_272008_272455_269729_271689_272821_273094_273161_273121_273301_270055_273704_273734_274177_269610_273917_274234_273043_272806_272560_272802_188331; BAIDUID_BFESS=20B48AA69066FECF934B15B17EDBCE81:FG=1; ZFY=TqDMr4CQ1E3qObSoDd5ZpZzs2dlnQb6WS4jfek09Yz4:C; BDUSS=ktsbmgxRGM4eVlPOTRoT243MDBXYk9JVW5OfnpIfmQyVk1GZ201bW1vSmpJa0psRVFBQUFBJCQAAAAAAAAAAAEAAAAnaTy8bm1jdmLM7NCrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGOVGmVjlRplR; BDUSS_BFESS=ktsbmgxRGM4eVlPOTRoT243MDBXYk9JVW5OfnpIfmQyVk1GZ201bW1vSmpJa0psRVFBQUFBJCQAAAAAAAAAAAEAAAAnaTy8bm1jdmLM7NCrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGOVGmVjlRplR; BA_HECTOR=20a5a0a4200la0al2g858ka31ihnq5c1o; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=2; delPer=0; COOKIE_SESSION=1152360_1_4_4_17_12_0_0_4_4_3_4_1292665_0_10_0_1696331977_1695037978_1696331967%7C9%23105792_16_1695037963%7C9; ab_sr=1.0.1_ZjU3MzFkNWZkYzk3MmEwYTljYmYyNTU0NmQ0ZWM2YzQ2ZWQ0YWQ5ZTdlY2UzZmEzMjI5OWJlZTMyYmUxOWRiYTJhMTFkYmVkNmVkNTBjZDdjOWY1OWRiNWFjMDAwMTkxYjQ1NmIzZWQwZTg4YjBmYTA1MTQzZDc5ZTRmYmRkNzE2MDFiODk5OWZiNDQ5MjU3OWYyMmY3YmJmYmM5OTdhZA==; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; B64_BOT=1; H_PS_PSSID=26350; H_PS_645EC=67f4xc91orAdYSXlMs79uvmcu2dWFH6ZHzDvDhWM80IxpmIAkG51W1C%2FneY0DaFGoUIb0WqONRc; BDORZ=FFFB88E999055A3F8A630C64834BD6D0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入开始的页码:"))
    end_page = int(input("请输入结束的页码:"))
    for page in range(start_page, end_page + 1):
        # 每一页都有自己的请求对象的定制
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # 下载
        down_load(page, content)
