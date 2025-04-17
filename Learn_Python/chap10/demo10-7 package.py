# 第三方模块的安装与卸载

# requests库，是用于处理HTTP(Hypertext Transfer Protocol)请求的第三方库,该库在爬虫程序中使用频率极高
# 使用requests库中的get()函数可以打开一个网络请求，并获取一个Response响应对象。
# 响应结果中的字符串数据可以通过响应对象的text属性获取，响应结果中除了有字符串数据也有二进制数据，
# 响应结果中的二进制数据可以通过响应对象的content属性获取。

import requests
import re
url = 'https://www.weather.com.cn/weather1d/101010100.shtml'    # 爬虫打开浏览器上的网页
response = requests.get(url)                                    # 打开浏览器并打开网址
response.encoding = 'utf-8'
print(response.text)                                            # 打印响应对象中的字符串数据

city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', response.text)         # 正则表达式匹配城市名称
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', response.text)
wd = re.findall('<span class="wd">(.*)</span>', response.text)
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', response.text)

print(city)
print(weather)
print(wd)
print(zs)

lst = []
for a, b, c, d in zip(city, weather, wd, zs):
    lst.append([a, b, c, d])
print(lst)
for item in lst:
    print(item)
'''
<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">24/32℃</span>
<span class="zs">适宜</span>
'''

url1 = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
resp = requests.get(url1)

# 保存到本地
with open('logo.png', 'wb') as file:
    file.write(resp.content)          # 将响应对象中的二进制数据写入到文件中 

