"""Winston_freshmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,include

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^tinymce/', include('tinymce.urls')), # 富文本编辑器
    re_path(r'^search', include('haystack.urls')), # 全文检索框架
    re_path(r'^user/', include(('user.urls','user'), namespace='user')), # 用户模块
    re_path(r'^cart/', include(('cart.urls','cart'), namespace='cart')), # 购物车模块
    re_path(r'^order/', include(('order.urls','order'), namespace='order')), # 订单模块
    re_path(r'^', include(('goods.urls','goods'), namespace='goods')), # 商品模块
]

admin.site.site_header = '宅食尚品'
admin.site.site_title = '后台管理'