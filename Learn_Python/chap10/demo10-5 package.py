# datetime模块可以更方便地显示日期并对日期进行运算
# datetime.datetime             # 表示日期时间的类
# datetime.timedelta            # 表示时间间隔的类
# datetime.date                 # 表示日期的类
# datetime.time                 # 表示时间的类
# datetime.tzinfo               # 时区相关的类

from datetime import datetime   # 导入datetime模块中的datetime类
dt = datetime.now()            # 获取当前日期时间
print(dt)                      # 输出当前日期时间

# datetime是一个类，手动创建这个类的对象
# 需要传入参数：年、月、日、时、分、秒、微秒
dt2 = datetime(2028, 8, 8, 20, 8)
print('dt2的数据类型',type(dt2),'dt2所表示的日期时间',dt2)
print('dt2的年份',dt2.year)         # dt2的年份
print('dt2的月份',dt2.month)        # dt2的月份
print('dt2的日期',dt2.day)          # dt2的日期
print('dt2的小时',dt2.hour)        # dt2的小时
print('dt2的分钟',dt2.minute)      # dt2的分钟
print('dt2的秒数',dt2.second)      # dt2的秒数
print('dt2的微秒数',dt2.microsecond)  # dt2的微秒数

# 比较两个datetime类型对象的大小
labor_day = datetime(2028, 5, 1, 0, 0, 0)
national_day = datetime(2028, 10, 1, 0, 0, 0)
print('labor day in 2028 is earlier than national day in 2028?',
      labor_day < national_day)  # True

# datetime类型与字符串进行转换
nowdt = datetime.now()  # 获取当前日期时间
nowdt_str = nowdt.strftime('%Y/%m/%d %H:%M:%S')  # 转换为字符串
print('nowdt的数据类型', type(nowdt), 'nowdt的值', nowdt)  # datetime类型
print('nowdt_str的数据类型', type(nowdt_str), 'nowdt_str的值', nowdt_str)  # str类型

# 将字符串转换为datetime类型
str_datetime = '2028年8月8日 20时8分'
dt3 = datetime.strptime(str_datetime, '%Y年%m月%d日 %H时%M分')
print('str_datetime的数据类型', type(str_datetime), 'str_datetime的值', str_datetime)  # str类型
print('dt3的数据类型', type(dt3), 'dt3的值', dt3)  # datetime类型