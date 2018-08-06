from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from admin_user.functions import get_check_code_info
from main import models


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


def products_list(request):
    """
    产品清单
    :param request:
    :return:
    """
    if request.method == 'GET':
        request.session['emp_id'] = 1
        if request.session.get('emp_id'):
            emp_id = request.session.get('emp_id')
            store_info_id = models.EmpInfo.objects.filter(emp_id=emp_id).first().store_info_id
            goods_info_list = {goods.name: goods.price for goods in
                               models.GoodsInfo.objects.filter(store_info_id=store_info_id).all()}
            data = {
                'code': 200,
                'msg': '请求成功',
                'result': goods_info_list
            }
            return JsonResponse(data)
        else:
            data = {
                'code': 301,
                'msg': '请求失败'
            }
            return JsonResponse(data)
