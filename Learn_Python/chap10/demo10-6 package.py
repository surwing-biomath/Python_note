from datetime import datetime
from datetime import timedelta

# 创建两个datetime类型的对象
delta1 = datetime(2028, 10, 1) - datetime(2028, 5, 1)
print('delta1的数据类型', type(delta1), 'delta1的值', delta1)  # timedelta类型
print('2028年5月1日之后的153天是:', datetime(2028, 5, 1) + delta1)

# 通过传入参数的方式创建timedelta类型的对象
td1 = timedelta(10)
print('创建一个10天的timedelta对象', td1)
td2 = timedelta(10, 11)
print('创建一个10天11秒的timedelta对象', td2)

