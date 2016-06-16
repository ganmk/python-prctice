# 当函数的参数不确定时，可以使用*args和**kwargs。*args没有key值，**kwargs有key值

def fun_var_args(farg, *args):
    print 'args:', farg
    for value in args:
        print 'another arg:',value

# *args可以当作可容纳多个变量组成的list或tuple
fun_var_args(1, 'two', 3, None)
#args: 1
#another arg: two
#another arg: 3
#another arg: None


def fun_var_kwargs(farg, **kwargs):
    print 'args:',farg
    for key in kwargs:
        print 'another keyword arg:%s:%s' % (key, kwargs[key])

# myarg1,myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary
fun_var_kwargs(1, myarg1='two', myarg2=3, myarg3=None)

# 输出：
#args: 1
#another keyword arg:myarg1:two
#another keyword arg:myarg2:3
#another keyword arg:myarg3:None


