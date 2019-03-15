from django.db import models
import time
from datetime import datetime
# Create your models here.
'''
1、模型可以帮我们,连接数据库, 获取数据库中的信息
'''
class Users(models.Model):
    '''自定义Stu表对应的Model类'''
    #定义属性：默认主键自增id字段可不写
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('姓名',max_length=32)
    email = models.CharField('Email',max_length=100)
    cdate = models.DateTimeField('创建日期')

    # 定义默认输出格式
    def __str__(self):
        return "%d:%s:%s:%s"%(self.id,self.name,self.email,self.cdate)

    # 自定义对应的表名，默认表名：myapp_stu
    class Meta:
        db_table="users" # 定义连接数据库时，是blogdb下的users表格
        
        verbose_name_plural = '用户信息管理'
        verbose_name = '需要修改的用户'