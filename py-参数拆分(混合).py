# 两者都有
def fun_args_kwargs(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs


args = [1, 2, 3, 4]
kwargs = {'name': 'BeginMan', 'age': 22}
fun_args_kwargs(args,kwargs)
#args: ([1, 2, 3, 4], {'age': 22, 'name': 'BeginMan'})
#kwargs: {}

fun_args_kwargs(1,2,3,a=100)
#args: (1, 2, 3)
#kwargs: {'a': 100}
