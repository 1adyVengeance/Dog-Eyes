from django.http import JsonResponse

from main import code_status, models


def products_list(request):
    """
    产品
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 查询商品清单
        request.session['emp_id'] = 1
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
        store_info_id = request.POST.get('store_info_id')
        goods_type_id = request.POST.get('goods_type_id')
        name = request.POST.get('name')
        price = request.POST.get('price')

        try:
            create = models.GoodsInfo.objects.create(store_info_id=store_info_id, goods_type_id=goods_type_id,
                                                     name=name, price=price)
            data = code_status.SUCCESS
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'DELETE':
        # 删除商品
        goods_id = request.GET.get('goods_id')
        goods = models.GoodsInfo.objects.filter(goods_id=goods_id)
        try:
            delete = goods.delete()
            data = code_status.SUCCESS
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'PATCH':
        # 修改商品信息
        store_info_id = request.POST.get('store_info_id')
        goods_type_id = request.POST.get('goods_type_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        goods_id = request.GET.get('goods_id')
        goods = models.GoodsInfo.objects.filter(goods_id=goods_id)
        try:
            updata = goods.update(store_info_id=store_info_id, goods_type_id=goods_type_id,
                         name=name, price=price)
            data = code_status.SUCCESS
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
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'DELETE':
        # 删除商品
        goods_type_name = request.GET.get('name')
        goods = models.GoodsType.objects.filter(name=goods_type_name)
        try:
            delete = goods.delete()
            data = code_status.SUCCESS
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
    if request.method == 'POST':
        goods_id = request.GET.get('goods_id')
        material_info_id = request.POST.get('material_info_id')
        need_count = request.POST.get('need_count')
        unit = request.POST.get('unit')
        try:
            create = models.Recipe.objects.create(goods_id=goods_id, material_info_id=material_info_id,
                                                  need_count=need_count, unit=unit)
            data = code_status.SUCCESS
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'DELETE':
        # 删除配方
        goods_id = request.GET.get('goods_id')
        recipe = models.Recipe.objects.filter(goods_id=goods_id).first()
        try:
            delete = recipe.delete()
            data = code_status.SUCCESS
            return JsonResponse(data)
        except:
            data = code_status.DATABASE_ERROR
            return JsonResponse(data)

    if request.method == 'GET':
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

