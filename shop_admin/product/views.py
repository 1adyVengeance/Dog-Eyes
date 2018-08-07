from datetime import datetime

from django.http import JsonResponse

from main import code_status, models


def product_update(request):
    """
    修改商品信息
    :param request:
    :return:
    """
    request.session['emp_id'] = 1
    if request.method == 'POST':
        emp_id = request.session.get('emp_id')
        store_info_id = request.POST.get('store_info_id')
        goods_type_id = request.POST.get('goods_type_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        goods_id = request.GET.get('goods_id')
        try:
            goods = models.GoodsInfo.objects.filter(goods_id=goods_id)
            goods.update(store_info_id=store_info_id, goods_type_id=goods_type_id, name=name, price=price)
            data = code_status.SUCCESS
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '修改商品{}信息'.format(name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)


def products_list(request):
    """
    产品
    :param request:
    :return:
    """
    request.session['emp_id'] = 1
    if request.method == 'GET':
        # 查询商品清单
        if request.session.get('emp_id'):
            emp_id = request.session.get('emp_id')
            store_info_id = models.EmpInfo.objects.filter(emp_id=emp_id).first().store_info_id
            goods_info_list = models.GoodsInfo.objects.filter(store_info_id=store_info_id)
            goods_info = [i.to_dict() for i in goods_info_list]
            data = code_status.SUCCESS
            data['result'] = goods_info
            return JsonResponse(data)

    if request.method == 'POST':
        # 新增商品
        emp_id = request.session.get('emp_id')
        store_info_id = request.POST.get('store_info_id')
        goods_type_id = request.POST.get('goods_type_id')
        name = request.POST.get('name')
        price = request.POST.get('price')

        try:
            create = models.GoodsInfo.objects.create(store_info_id=store_info_id, goods_type_id=goods_type_id,
                                                     name=name, price=price)
            data = code_status.SUCCESS
            create.save()
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '新增商品{}'.format(name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'DELETE':
        # 删除商品
        emp_id = request.session.get('emp_id')
        goods_id = request.GET.get('goods_id')
        goods = models.GoodsInfo.objects.filter(goods_id=goods_id)
        try:
            delete = goods.delete()
            data = code_status.SUCCESS
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '新增商品{}'.format(goods.first().name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)


def goods_type_update(request):
    """
    修改分类信息
    :param request:
    :return:
    """
    request.session['emp_id'] = 1
    if request.method == 'POST':
        emp_id = request.session.get('emp_id')
        goods_type_id = request.GET.get('goods_type_id')
        new_name = request.POST.get('name')
        try:
            goods = models.GoodsType.objects.filter(goods_type_id=goods_type_id)
            name = goods.first().name
            goods.update(name=new_name)
            data = code_status.SUCCESS
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '修改分类{}为{}'.format(name, new_name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)


def goods_type(request):
    """
    商品类型
    :param request:
    :return:
    """
    request.session['emp_id'] = 1
    if request.method == 'GET':
        # 查询商品类型清单
        if not request.GET.get('name'):
            emp_id = request.session.get('emp_id')
            store_info_id = models.EmpInfo.objects.filter(emp_id=emp_id).first().store_info_id
            types = models.GoodsType.objects.filter(store_info_id=store_info_id)
            type_list = [type.name for type in types]
            data = code_status.SUCCESS
            data['type_list'] = type_list
            return JsonResponse(data)
        if request.GET.get('name'):
            name = request.GET.get('name')
            type_obj = models.GoodsType.objects.filter(name=name).first()
            if type_obj:
                data = code_status.SUCCESS
                data['result'] = type_obj.to_dict()
                return JsonResponse(data)
            else:
                data = code_status.SUCCESS
                data['result'] = '当前没有此分类'
                return JsonResponse(data)

    if request.method == 'POST':
        # 新增分类
        emp_id = request.session.get('emp_id')
        store_info_id = models.EmpInfo.objects.filter(emp_id=emp_id).first().store_info_id
        name = request.POST.get('name')
        try:
            create = models.GoodsType.objects.create(store_info_id=store_info_id, name=name)
            data = code_status.SUCCESS
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '新增分类{}'.format(name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'DELETE':
        # 删除商品
        emp_id = request.session.get('emp_id')
        goods_type_name = request.GET.get('name')
        goods = models.GoodsType.objects.filter(name=goods_type_name)
        try:
            delete = goods.delete()
            data = code_status.SUCCESS
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '删除分类{}'.format(goods_type_name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)


def recipe(request):
    """
    商品配方
    :param request:
    :return:
    """
    request.session['emp_id'] = 1
    if request.method == 'POST':
        # 新增配方
        emp_id = request.GET.get('emp_id')
        goods_id = request.GET.get('goods_id')
        material_info_id = request.POST.get('material_info_id')
        need_count = request.POST.get('need_count')
        unit = request.POST.get('unit')
        try:
            create = models.Recipe.objects.create(goods_id=goods_id, material_info_id=material_info_id,
                                                  need_count=need_count, unit=unit)
            data = code_status.SUCCESS
            create.save()
            goods_name = models.GoodsInfo.objects.filter(goods_id=goods_id).first().name
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '新增{}的配方'.format(goods_name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'DELETE':
        # 删除配方
        emp_id = request.POST.get('emp_id')
        goods_id = request.GET.get('goods_id')
        recipe = models.Recipe.objects.filter(goods_id=goods_id).first()
        try:
            recipe.delete()
            data = code_status.SUCCESS
            goods_name = models.GoodsInfo.objects.filter(goods_id=goods_id).first().name
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '删除{}的配方'.format(goods_name)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'GET':
        # 查询配方
        goods_id = request.GET.get('goods_id')
        if goods_id:
            recipes = models.Recipe.objects.filter(goods_id=goods_id)
            recipe_info = [recipe.to_dict() for recipe in recipes]
            data = code_status.SUCCESS
            data['result'] = recipe_info
            return JsonResponse(data)
        else:
            recipes = models.Recipe.objects.all()
            recipe_info = [recipe.to_dict() for recipe in recipes]
            data = code_status.SUCCESS
            data['result'] = recipe_info
            return JsonResponse(data)


def recipe_update(request):
    """
    修改配方信息
    :param request:
    :return:
    """
    request.session['emp_id'] = 1
    if request.method == 'POST':
        emp_id = request.session.get('emp_id')
        recipe_id = request.GET.get('recipe_id')
        old_name = request.GET.get('name')
        new_name = request.POST.get('name')
        need_count = request.POST.get('need_count')
        unit = request.POST.get('unit')
        try:
            # old_material = models.MaterialInfo.objects.filter(name=old_name)
            new_models = models.MaterialInfo.objects.filter(name=new_name)
            new_material_info_id = new_models.first().material_info_id
            recipe = models.Recipe.objects.filter(recipe_id=recipe_id)
            recipe.update(material_info_id=new_material_info_id, need_count=need_count)
            data = code_status.SUCCESS
            handle_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            event = '修改配方{}为{}{}{}'.format(old_name, new_name, need_count, unit)
            models.EmpHandleLog.objects.create(emp_id=emp_id, handle_time=handle_time, event=event)
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

