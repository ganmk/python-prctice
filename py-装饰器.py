def login(func):
    print 'login'
    return func#只返回func函数的内存地址，不调用func

def tv(name):
    print '%s to tvpage' % name

f = login(tv)
f('ahaii')
