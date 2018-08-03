from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

from main.models import MaterialType, MaterialInfo

# Create your views here.
def show_all_material_type(request):
    """
    查询所有的原料分类标签
    :return: json格式
    """
    if request.method == 'GET':
        material_types = MaterialType.objects.all()
        material_type_list = []
        for type in material_types:
            material_type_list.append(model_to_dict(type))
        data = {'code':200,'material_type_list':material_type_list}
        return JsonResponse(data=data)


def get_material_type_by_id(request,id):
    """
    按id查询原料分类标签
    :param id: 原料分类id
    :return: 返回查询成功或失败的json结果
    """
    if request.method == 'GET':
        material_type = MaterialType.objects.filter(material_type_id=id).first()
        if not material_type:
            data = {'code':1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data=data)
        material_type_dict = model_to_dict(material_type)
        data = {'code': 200, 'material_type_dict':material_type_dict}
        return JsonResponse(data=data)


def change_material_type_info(request):
    """
    增加/修改原料分类信息
    :return: 返回成功/错误信息JSON
    """
    if request.method == 'POST':
        type_id = request.POST.get('id')
        is_delete = request.POST.get('is_delete')
        # 如果type_id有值，进行修改操作，否则是新增
        if type_id:
            material_type = MaterialType.objects.filter(material_type_id=type_id).first()
            material_type.is_delete = is_delete
            material_type.save()
            data = {'code': 200,'msg': '修改成功'}
            return JsonResponse(data=data)
        name = request.POST.get('name')
        merchant_id = 1
        emp_id = 1
        if not all([is_delete, name, merchant_id, emp_id]):
            data = {'code': 1001, 'msg': '请填写完整信息'}
            return JsonResponse(data=data)
        new_material_type = MaterialType(
            merchant_id=merchant_id,
            name=name,
            emp_id=emp_id,
            is_delete=is_delete
        )
        new_material_type.save()
        data = {'code': 200, 'msg': '保存成功'}
        return JsonResponse(data=data)


def show_all_material(request):
    """
    展示所有的原料信息
    :return: 返回所有的原料信息JSON
    """
    if request.method == 'GET':
        materials = MaterialInfo.objects.all()
        material_list = []
        for material in  materials:
            material_list.append(model_to_dict(material))
        data = {'code': 200, 'material_list': material_list}
        return JsonResponse(data=data)


def get_material_by_id(request, id):
    """
    通过原料id查询原料信息
    :param request:
    :param id: 原料id
    :return: 返回查询成功/失败的JSON信息
    """
    if request.method == 'GET':
        material = MaterialInfo.objects.filter(material_info_id=id).first()
        if not material:
            data = {'code':1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data)
        material_dict = model_to_dict(material)
        data = {'code':200, 'material_dict': material_dict}
        return JsonResponse(data)


def get_materials_by_type(request, type_id):
    """
    通过原料分类查询原料信息
    :param type_id: 原料分类id
    :return: 返回查询成功/失败的JSON信息
    """
    if request.method == 'GET':
        type = MaterialType.objects.filter(material_type_id=type_id).first()
        if not type:
            data = {'code': 1000, 'msg': '没有找到对应的信息'}
            return JsonResponse(data)
        materials = type.materialinfo_set.all()
        if not materials:
            data = {'code': 1002, 'msg': '该分类没有数据'}
            return JsonResponse(data)
        material_list = []
        for material in materials:
            material_list.append(model_to_dict(material))
        data = {'code': 200, 'material_list': material_list}
        return JsonResponse(data=data)


def change_material_info(request):
    """
    新增/修改原料信息
    :return: 返回成功/失败结果JSON
    """
    if request.method == 'POST':
        material_id = request.POST.get('id')
        type_id = request.POST.get('type_id')
        name = request.POST.get('name')
        if not all([type_id, name]):
            data = {'code': 1001, 'msg': '请填写完整信息'}
            return JsonResponse(data=data)
        # 如果原料id有值，修改信息，否则新增信息
        if material_id:
            material = MaterialInfo.objects.filter(material_info_id=material_id).first()
            material.material_type_id = type_id
            material.name = name
            material.save()
            data = {'code': 200, 'msg': '修改成功'}
            return JsonResponse(data=data)
        new_material = MaterialInfo(
            material_type_id=type_id,
            name=name
        )
        new_material.save()
        data = {'code': 200, 'msg': '保存成功'}
        return JsonResponse(data=data)
