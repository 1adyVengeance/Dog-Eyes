from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

from main.models import MaterialType

# Create your views here.
def show_all_material_type(request):
    if request.method == 'GET':
        material_types = MaterialType.objects.all()
        material_type_list = []
        for type in material_types:
            material_type_list.append(model_to_dict(type))
        data = {'code':200,'material_type_list':material_type_list}
        return JsonResponse(data=data)