# 递归函数：
# 递归：在一个函数的函数体内调用该函数本身，该函数就是递归函数
# 一个完整的递归操作由两部分组成，一部分是递归调用，一部分是递归终止条件，一般可使用if-else结构来判断递归的调用和递归的终止
# 优点：思路与代码比较简单，缺点：占用内存比较多，效率比较低

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(5))

def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(20))