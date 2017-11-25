from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import render, loader


# Create your views here.
def homePage(request):
    temp = loader.get_template('wx.html')
    conx = {'name': 'dk', 'age': 24, 'sex': 'MV', 'home': 'FuYang'}
    return HttpResponse(render(request, 'wx.html', conx))
