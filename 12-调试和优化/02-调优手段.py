# 1， timer   定制定时器  获取函数的执行时间  但是无发进入细节
import time
import requests

# 方法一
start = time.time()
requests.get('https://www.cnblogs.com/liaocheng/p/5421818.html')
print('cost : {}s'.format(time.time() - start))


# 方法二
def time_it(func):
    def wrapper(*args, **kw):
        start = time.time()
        results = func(*args, **kw)
        print(func.__name__, 'cost : {}s'.format(time.time() - start))
        return results
    return wrapper

@time_it
def func_test():
    requests.get('https://www.cnblogs.com/liaocheng/p/5421818.html')

# func_test()


# 2. profile/cProfile   可以进入程序执行的过程
import cProfile


def loop(count):
    result = []
    for i in range(count):
        result.append(i)


cProfile.run('loop(100000)')

"""
Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.052    0.052    0.075    0.075 02-调优手段.py:30(loop)
        1    0.004    0.004    0.080    0.080 <string>:1(<module>)
        1    0.000    0.000    0.080    0.080 {built-in method builtins.exec}
   100000    0.024    0.000    0.024    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

ncalls: 执行行数
tottime: 总执行时间
percall: 平均执行时间
cumtime: 累计执行时间
percall: 平均每次执行时间
filename:lineno(function):   具体执行说明

"""
import pstats
from io import StringIO
pr = cProfile.Profile()


def loop1(count):
    result = []
    for i in range(count):
        result.append(i)

pr.enable()
loop(100000)
pr.disable()

s = StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()
print(s.getvalue())
