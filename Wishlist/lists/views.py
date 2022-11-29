from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
