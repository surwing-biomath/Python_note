# 函数的返回值return：
# 1，如果函数的运行结果需要在其他函数中使用，那么这个函数应该被定义成带返回值的函数
# 2，函数的运行结果使用return关键字进行返回，返回给函数的调用处
# 3，return可以出现在函数中的任意一个位置，用于结束函数
# 4，返回值可以是一个值，或多个值，如果返回的值是多个，结果是一个元组类型

# 函数的返回值
def calc(a,b):
    print(a+b)

calc(1,2)
print(calc(1,2))    # None

def calc2(a,b):
    s=a+b
    return s

get_s=calc2(1,2)
print(get_s)
get_s2=calc2(calc2(1,2),3)
print(get_s2)

# 返回值可以是多个
def get_sum(num):
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if i%2!=0:
            odd_sum+=i
        else:
            even_sum+=i
        s+=i
    return odd_sum,even_sum,s

result=get_sum(10)
print(type(result),result)     # <class 'tuple'> (25, 30, 55)
# 解包赋值
a,b,c=get_sum(10)
print(a,b,c)
