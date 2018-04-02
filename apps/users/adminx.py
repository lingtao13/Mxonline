# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/3/14 下午12:34'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True



class GlobalSettings(object):
    # 标题
    site_title = 'mx后台管理系统'
    # 页脚信息
    site_footer = 'mxonline.com'
    # APP折叠
    menu_style = 'accordion'




class EmailVerifyRecordAdmin(object):

    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):

    list_display = ['title', 'image','url', 'index','add_time']
    search_fields = ['title', 'image','url', 'index']
    list_filter = ['title', 'image','url', 'index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
# 注册主题风格
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 注册标题信息
xadmin.site.register(views.CommAdminView, GlobalSettings)