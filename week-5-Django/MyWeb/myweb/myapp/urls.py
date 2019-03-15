''' 子路由 '''
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^aa$', views.index), # ^$ 是什么意思
    # ^$ 表示什么都没写, 因此, 也就直接访问 views.index
    # ^: 表示行的 开始
    # $: 表示行的 结尾

    url(r'^users$',views.users),
]
