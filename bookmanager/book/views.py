from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是python函数
视图函数有两个要求：
    1. 视图函数的第一个参数就是接收的请求
    2. 必须返回一个相应
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse


# 我们希望用户输入 http://127.0.0.1:8000/index/
# 来访问视图函数
def index(request):
    # return HttpResponse('ok')
    # 模拟数据查询
    context = {
        'name': '马上双十一，点击有惊喜'
    }
    # render参数解析
    # 第一个是request
    # 第二个是模板的在settings里面目录下的存放位置
    # context是html中要被替换的数据
    return render(request, 'book/index.html', context=context)  # render就是渲染模板的意思
