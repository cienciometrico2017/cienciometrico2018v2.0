from django.core import serializers
from django.shortcuts import render
from apps.palabraClave.models import palabraClave

from django.http import JsonResponse

def view(request):
    palabras = palabraClave.objects.all()
    posts_serialized = serializers.serialize('json', palabras)
    return JsonResponse(posts_serialized, safe=False)
