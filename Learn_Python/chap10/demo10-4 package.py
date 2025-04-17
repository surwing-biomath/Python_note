# Python中常用的内置模块
# 在安装Python解释器时与解释器一起安装进来的模块被称为系统内置模块，也被称为标准模块或标准库
# 标准库名称及其功能描述：
# os模块：              与操作系统和文件相关操作有关的模块
# re模块：              用于在Python的字符串中执行正则表达式的模块
# random模块：          用于产生随机数的模块
# json模块：            用于对高维数据进行编码和解码的模块
# time模块：            与时间相关的模块
# datetime模块：        与日期时间相关的模块，可以方便的显示日期并对日期进行运算

# random模块：Python中用于产生随机数的标准库
# 函数名称及功能描述：
# seed(x):              初始化给定的随机数种子，默认为当前系统时间
# random():             产生一个[0.0,1.0)之间的随即小数
# randint(a,b):         生成一个[a,b]之间的整数
# randrange(m,n,k):     生成一个[m,n)之间步长为k的随机整数
# uniform(a,b):         生成一个[a,b]之间的随即小数
# choice(seq):          从序列中随机选择一个元素
# shuffle(seq):         将序列seq中元素随机排列，返回打乱后的序列

# 导入
import random
# 设置随机数的种子
random.seed(10)
print(random.random())                      # 0.5714025946899135
print(random.random())                      # 0.4288890546751146
print('-'*50)

random.seed(10)
print(random.randint(1,100))                # 74
print('-'*50)

for i in range(10):                         # 1       4       4       7       1       1       4       4       4       7
    print(random.randrange(1,10,3),end='\t')
print()
print('-'*50)

print(random.uniform(1,100))                # 81.25126013057475
print('-'*50)

lst=[i for i in range(1,11)]
print(random.choice(lst))                   # 1
print('-'*50)

random.shuffle(lst)
print(lst)                                  # [5, 4, 10, 7, 3, 2, 1, 6, 8, 9]
random.shuffle(lst)
print(lst)                                  # [3, 4, 5, 6, 8, 10, 7, 1, 2, 9]
print('-'*50)

# time模块是Python中提供的用于处理时间的标准库，可以用来进行时间处理、时间格式化和计时等
# 函数名称及功能描述
# time():                                   获取当前时间戳
# localtime(sec):                           获取指定时间戳对应的本地时间的struct_time对象
# ctime():                                  获取当前时间戳对应的易读字符串
# strftime():                               格式化时间，结果为字符串
# strptime():                               提取字符串的时间，结果为struct_time对象
# sleep(sec):                               休眠sec秒

# time模块中的格式化字符串及日期/时间及取值范围
# %Y            年份            0001~9999
# %m            月份            01~12
# %B            月名            January~December
# %d            日期            01~31
# %A            星期            Monday~Sunday
# %H            小时（24h制）    00~23
# %i            小时（12h制）    01~12
# %M            分钟            00~59
# %S            秒              00~59

import time
now=time.time()
print(now)                                  # 1736320051.2412353

obj=time.localtime()                        # struct_time对象
print(obj)                                  # time.struct_time(tm_year=2025, tm_mon=1, tm_mday=8, tm_hour=15, tm_min=7, tm_sec=31, tm_wday=2, tm_yday=8, tm_isdst=0)

obj2=time.localtime(60)                     # 60秒，1970年，1月1日，8时，1分，0秒
print(obj2)                                 # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=1, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
print(type(obj2))                           # <class 'time.struct_time'>
print('年份：',obj2.tm_year)                # 年份： 1970
print('月份：',obj2.tm_mon)                 # 月份： 1
print('日期：',obj2.tm_mday)                # 日期： 1
print('时：',obj2.tm_hour)                  # 时： 8
print('分：',obj2.tm_min)                   # 分： 1
print('秒：',obj2.tm_sec)                   # 秒： 0
print('星期：',obj2.tm_wday)                # 星期： 3              # [0,6],i表示星期i+1
print('今年的多少天：',obj2.tm_yday)         # 今年的多少天： 1
# 时间戳对应的易读的字符串：
print(time.ctime(1736320469.327881))                 # Wed Jan  8 15:14:29 2025
# 日期时间格式化
print(time.strftime('%Y-%m-%d',time.localtime()))   # 2025-01-08
print(time.strftime('%H:%M:%S',time.localtime()))   # 15:22:49
print(time.strftime('%B',time.localtime()))         # January
print(time.strftime('%A',time.localtime()))         # Wednesday

# 字符串转成struct_time
print(time.strptime('2008-08-08','%Y-%m-%d'))       # time.struct_time(tm_year=2008, tm_mon=8, tm_mday=8, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=221, tm_isdst=-1)

time.sleep(20)
print('helloworld')

