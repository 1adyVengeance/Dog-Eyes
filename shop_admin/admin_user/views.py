from datetime import datetime

import pymysql
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from admin_user.functions import get_check_code_info
from main import models, code_status


def check_code(request):
    code, image = get_check_code_info()
    data = {
        'code': code,
        'image': image
    }
    return JsonResponse(data)


def login(request):
    """
    登陆
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'Admin/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.AdminInfo.objects.filter(name=username).first()
        if username and password:
            if not user:
                msg = '用户名不存在!'
                return HttpResponseRedirect(reverse('admin_user:login'))
            elif password != user.password:
                msg = '密码不正确!'
                return HttpResponseRedirect(reverse('admin_user:login'))
            else:
                msg = '登陆成功'
                admin_id = user.admin_id
                login_ip = request.META['REMOTE_ADDR']
                login_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                models.AdminLoginLog.objects.create(login_ip=login_ip, login_time=login_time, admin_id=admin_id)
                request.session['is_login'] = 'true'
                request.session['user'] = username
                return HttpResponseRedirect(reverse('admin_user:index'))


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    try:
        # 删除is_login对应的value值
        del request.session['is_login']
        del request.session['user']
    except KeyError:
        pass
    # 点击注销之后，直接重定向回登录页面
    return HttpResponseRedirect(reverse('admin_user:login'))


def index(request):
    """
    首页
    :param request:
    :return:
    """
    if request.method == 'GET':
        if request.session.get('user'):
            return render(request, 'Admin/index.html')
        else:
            return HttpResponseRedirect(reverse('admin_user:login'))


def login_log(request):
    """
    登陆日志
    :param request:
    :return:
    """





