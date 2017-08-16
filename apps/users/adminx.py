# -*- coding:utf-8 -*-
# __author__ = 'hai'
# __date__ = '2017/8/15 22:31'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    """
    xadmin主题配置
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    xadmin全局配置
    """
    # 替换左上角默认文字、以及后天页面的title文字
    site_title = '后台管理系统'
    # 替换底部默认文字
    site_footer = '在线课程网'
    # 对左侧导航栏进行设置
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    """轮播图注册"""
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 注册主题功能
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 注册xadmin全局配置
xadmin.site.register(views.CommAdminView, GlobalSettings)

