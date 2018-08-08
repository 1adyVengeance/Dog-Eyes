from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from main.models import AdminInfo, AdminRole, AdminPower
# Create your views here.


def get_admins(request):
    if request.method == 'GET':
        return render(request,'Admin/administrator.html')


def get_admin_info(request):
    if request.method == 'GET':
        return render(request,'Admin/admin_info.html')


def show_all_admin(request):
    """
    展示所有的管理员
    :return: 返回查询结果JSON
    """
    if request.method == 'GET':
        admins = AdminInfo.objects.all()
        admin_list = []
        for admin in admins:
            admin_list.append(model_to_dict(admin))
        data = {'code': 200, 'admin_list': admin_list}
        return JsonResponse(data)


def get_admin_by_id(request, id):
    """
    通过管理员id查询
    :param id: 管理员id
    :return: 返回查询成功/失败信息JSON
    """
    if request.method == 'GET':
        admin = AdminInfo.objects.filter(admin_id=id).first()
        if not admin:
            data = {'code': 1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data)
        admin_dict = model_to_dict(admin)
        data = {'code': 200, 'admin_dict': admin_dict}
        return JsonResponse(data)


def get_admin_by_role_id(request, role_id):
    """
    通过角色id查询管理员
    :param role_id: 角色id
    :return: 返回查询成功/失败信息JSON
    """
    if request.method == 'GET':
        role = AdminRole.objects.filter(admin_role_id=role_id).first()
        if not role:
            data = {'code': 1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data)
        admins = role.admininfo_set.all()
        if not admins:
            data = {'code': 1003, 'msg': '该角色没有管理员'}
            return JsonResponse(data)
        admin_list = []
        for admin in admins:
            admin_list.append(model_to_dict(admin))
        data = {'code': 200, 'admin_list': admin_list}
        return JsonResponse(data)


def change_admin_info(request):
    """
    新增/更改管理员信息
    :return: 返回成功/失败信息JSON
    """
    if request.method == 'POST':
        admin_id = request.POST.get('id')
        role_id = request.POST.get('role_id')
        name = request.POST.get('name')
        leader_id = request.POST.get('leader_id')
        # is_delete = request.POST.get('is_delete')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        if not all([name, sex, phone_num]):
            data = {'code': 1004, 'msg': '请填写完整必填信息'}
            return JsonResponse(data=data)
        # admin_id有值，更改，否则新增
        if admin_id:
            admin = AdminInfo.objects.filter(admin_id=admin_id).first()
            admin.admin_role_id = role_id
            admin.name = name
            admin.leader_id = leader_id
            admin.sex = sex
            admin.age = age
            admin.phone_num = phone_num
            admin.email = email
            admin.save()
            data = {'code': 200, 'msg': '修改成功'}
            return JsonResponse(data=data)
        # 新增默认密码
        password = '123456'
        is_delete = 0
        new_admin = AdminInfo(
            admin_role_id=role_id,
            leader_id=leader_id,
            name=name,
            is_delete=is_delete,
            password=password,
            sex=sex,
            age=age,
            phone_num=phone_num,
            email=email
        )
        new_admin.save()
        data = {'code': 200, 'msg': '保存成功'}
        return JsonResponse(data=data)


def change_admin_status(request):
    if request.method == 'POST':
        admin_id = request.POST.get('id')
        is_delete = request.POST.get('is_delete')
        admin = AdminInfo.objects.filter(admin_id=admin_id).first()
        admin.is_delete = is_delete
        admin.save()
        data = {'code': 200, 'msg': '修改成功'}
        return JsonResponse(data=data)


def change_admin_passwd(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        old_passwd = request.POST.get('old_passwd')
        new_passwd = request.POST.get('new_passwd')
        c_mew_paswd = request.POST.get('c_mew_paswd')
        if new_passwd != c_mew_paswd:
            data = {'code': 1006, 'msg': '新密码不一致'}
            return JsonResponse(data=data)
        admin = AdminInfo.objects.filter(admin_id=id).first()
        if admin.password != old_passwd:
            data = {'code': 1007, 'msg': '原密码不正确'}
            return JsonResponse(data=data)
        admin.password = new_passwd
        admin.save()
        data = {'code': 200, 'msg': '修改成功'}
        return JsonResponse(data=data)


def show_all_role(request):
    """
    展示所有角色信息
    :return: 返回查询结果JSON
    """
    if request.method == 'GET':
        roles = AdminRole.objects.all()
        role_list = []
        for role in roles:
            role_list.append(model_to_dict(role))
        data = {'code': 200, 'role_list': role_list}
        return JsonResponse(data)


def get_role_by_id(request, id):
    """
    通过角色id查询
    :param id: 角色id
    :return: 返回查询成功/失败结果JSON
    """
    if request.method == 'GET':
        role = AdminRole.objects.filter(admin_role_id=id).first()
        if not role:
            data = {'code': 1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data)
        role_dict = model_to_dict(role)
        data = {'code': 200, 'role_dict': role_dict}
        return JsonResponse(data)


def change_role(request):
    """
    新增/更改角色信息
    :return: 返回成功/失败信息JSON
    """
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        is_delete = request.POST.get('is_delete')
        description = request.POST.get('description')
        if not all([name,is_delete, description]):
            data = {'code': 1001, 'msg': '请填写完整信息'}
            return JsonResponse(data=data)
        if id:
            role = AdminRole.objects.filter(admin_role_id=id).first()
            role.name = name
            role.is_delete = is_delete
            role.description = description
            role.save()
            data = {'code': 200, 'msg': '修改成功'}
            return JsonResponse(data=data)
        new_role = AdminRole(
            name=name,
            is_delete=is_delete,
            description=description
        )
        new_role.save()
        data = {'code': 200, 'msg': '保存成功'}
        return JsonResponse(data=data)


def show_all_power(request):
    """
    展示所有的权限
    :return: 返回查询的结果JSON
    """
    if request.method == 'GET':
        powers = AdminPower.objects.all()
        power_list = []
        for power in powers:
            power_list.append(model_to_dict(power))
        data = {'code': 200, 'power_list': power_list}
        return JsonResponse(data)


def get_power_by_id(request, id):
    """
    通过权限id查询
    :param id: 权限id
    :return: 返回查询成功/失败结果
    """
    if request.method == 'GET':
        power = AdminPower.objects.filter(admin_power_id=id).first()
        if not power:
            data = {'code': 1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data)
        power_dict = model_to_dict(power)
        data = {'code': 200, 'power_dict': power_dict}
        return JsonResponse(data)


def get_power_by_role_id(request, role_id):
    """
    通过角色id查询对应的权限
    :param role_id: 角色id
    :return: 返回查询成功/失败结果JSON
    """
    if request.method == 'GET':
        role = AdminRole.objects.filter(admin_role_id=role_id).first()
        if not role:
            data = {'code': 1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data)
        powers = role.adminpower_set.all()
        if not powers:
            data = {'code': 1005, 'msg': '该角色没有分配任何权限'}
            return JsonResponse(data)
        power_list = []
        for power in powers:
            power_list.append(power.to_dict())
        data = {'code': 200, 'power_list': power_list}
        return JsonResponse(data)


def change_power(request):
    """
    新增/更改权限信息
    :return: 返回成功/失败信息JSON
    """
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        if not all([name, description]):
            data = {'code': 1001, 'msg': '请填写完整信息'}
            return JsonResponse(data=data)
        # 如果id有值， 更改， 否则新增
        if id:
            power = AdminPower.objects.filter(admin_power_id=id).first()
            power.name = name
            power.description = description
            power.save()
            data = {'code': 200, 'msg': '修改成功'}
            return JsonResponse(data=data)
        new_power = AdminPower(
            name=name,
            description=description
        )
        new_power.save()
        data = {'code': 200, 'msg': '保存成功'}
        return JsonResponse(data=data)
