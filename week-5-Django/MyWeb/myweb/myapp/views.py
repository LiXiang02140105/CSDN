from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users
# Create your views here.
'''
视图:
    1、用来呈现数据 和 加载模板
    2、一定的操作, 包括数据库(已经在 models.py 中连接了数据库)
'''

def index(request):
    return HttpResponse("Hello Django!")


# 使用 数据库表 users

def users(request):
    mod = Users.objects
    list = mod.all()
    print(list)
    print(list[1],type(list[1]))

    return HttpResponse("OK") # 页面上