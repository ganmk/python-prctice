# 包裹关键字传递 dic是一个字典 收集所有的关键字传递给函数func_t
def func_t(**dic):
    print type(dic)
    print dic

print func_t(a=1, b=2)
print func_t(a=3, b=4, c=5)
