from django.http import HttpResponse
from django.shortcuts import render

from book.models import BookInfo


# Create your views here.
def index(request):
    # 在这里实现增删改查
    books = BookInfo.objects.all()
    print(books)

    return HttpResponse('index')


# # 增加数据###################################
# # 方式一
# from book.models import BookInfo
#
# book = BookInfo(
#     name='Django',
#     pub_date='2000-1-1',
#     read_count=10
# )
# # 必须调用对象的save方法才能将对象保存到数据库中
# book.save()
#
# # 方式二
# # objects -- 相当于一个代理，实现增删改查
# BookInfo.objects.create(
#     name='测试开发入门',
#     pub_date='2020-1-1',
#     read_count=100
# )
#
# # 修改数据###################################
# # 方式一
# # select * from BookInfo where id=6
# book = BookInfo.objects.get(id=6)
# book.name = '运维开发入门'
# book.save()
#
# # 方式二
# # filter 过滤
# BookInfo.objects.filter(id=6).update(name='爬虫入门', comment_count=666)
#
# # 删除数据###################################
# # 方式一
# book = BookInfo.objects.get(id=6)
# book.delete()
# BookInfo.objects.filter(id=6).delete()
#
# # 查询######################################
# # 查询单个
# try:
#     book = BookInfo.objects.get(id=1)  # 如果不存在会发生异常
# except BookInfo.DoesNotExist:
#     print('查询结果不存在')
# # 查询多个
# books = BookInfo.objects.all()
# from book.models import PeopleInfo
# PeopleInfo.objects.all()
#
# # count查询结果数量
# BookInfo.objects.all().count()
# BookInfo.objects.count()
#
# # 过滤查询############################
# # 实现SQL中的where功能，包括
# #
# # filter过滤出多个结果
# # exclude排除掉符合条件剩下的结果
# # get过滤单一结果
# # 语法
# # 模型类名.objects.filter(属性名__预算符=值)
#
# # 查询编号为1的图书
# book = BookInfo.objects.get(id=1)        # 简写形式
# book = BookInfo.objects.get(id__exact=1)  # 完整形式
#
# BookInfo.objects.get(pk=1)  # primary key主键
#
# BookInfo.objects.get(id=1)
# BookInfo.objects.filter(id=1)
#
# # 查询书名中包含“湖”的图书
# BookInfo.objects.filter(name__contains='湖')
#
# # 查询书名以“部”结尾的图书
# BookInfo.objects.filter(name__endswith='部')
#
# # 查询书名为空的图书
# BookInfo.objects.filter(name__isnull=True)
#
# # 查询编号为1或3或5的图书
# BookInfo.objects.filter(id__in=[1, 3, 5])
#
# # 查询编号大于3的图书
# # 大于（等于）gt(e)
# # 小于（等于）lt(e)
# BookInfo.objects.filter(id__gt=3)
#
# # 查询编号不等于3的书籍
# BookInfo.objects.exclude(id__exact=3)
#
# # 查询1980年发布的图书
# BookInfo.objects.filter(pub_date__year=1980)
#
# # 查询1990年1月1号后发布的图书
# BookInfo.objects.filter(pub_date__gt='1990-1-1')
