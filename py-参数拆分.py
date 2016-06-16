def fun_args(arg1, arg2, arg3):
    print 'arg1:', arg1
    print 'arg2:', arg2
    print 'arg3:', arg3

myargs = ['1', 'two', None]     # 定义列表
fun_args(*myargs)

# 输出：
#arg1: 1
#arg2: two
#arg3: None
