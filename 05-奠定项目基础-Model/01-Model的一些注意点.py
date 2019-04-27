
# 1.拆分setting一适应不同的环境

"""
QuerySet   django中我们与数据库所有的查询以及更新全部是有他来完成的
在MOdel层中  django提供了一个接口objects 以便于操作数据库


常用的接口字段：
all()       查询所有数据
filter()    根据条件查询  返回列表
exclude()   与filter相反  返回与条件相反的内容
reverse()   倒叙
distinct    去重查询  select distinct
none:  kong的queryset

不支持链式调用的接口：
get()
create()
get_or_create()
update_or_create()
latest()
earlieat()
first()
last()
exists()
bulk_create()
in_bluk()
update()
delete()
values()
value_list()


defer()   不需要展示的字段缓迟加载
only()    之获取   其他值在获取过程中会产生其他查询
select_related()  解决外键N+1 的方案
prefetch_related()  针对多对多  避免N+1的查询


contains   包含
icontains  包含 忽略大小写
exact     精确匹配
iexact 忽略大小写
in
gt
lt
gte
lte
startswith
istartswith  忽略大小写
endswith
iendswith
range 


F    执行数据层面的计算 避免数据竞争，
Q    解决or查询
SUM
Count

"""""