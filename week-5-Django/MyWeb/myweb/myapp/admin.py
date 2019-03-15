from django.contrib import admin

# Register your models here.
from myapp.models import Users
'''
    在后台管理器中，注册 数据库的管理 model
    以便能够直接在网页的 admin 路由下, 直接管理数据库
'''
# admin.site.register(Users) 

'''
    模型的管理器(装饰器写法)
    可以自定义显示的界面, 每个值都有自己所属的字段 列
''' 
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','name','email','cdate')

    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('id','name')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10

    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  #-id降序

    #list_editable 设置默认可编辑字段
    list_editable = ['email']
