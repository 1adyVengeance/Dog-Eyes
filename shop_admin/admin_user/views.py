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





