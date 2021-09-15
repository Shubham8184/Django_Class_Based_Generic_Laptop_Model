from django.shortcuts import render,redirect
from .models import LaptopModel
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class HomeView(View):
    def get(self,request):
        template_name='Home.html'
        return render(request,template_name)

class Laptoplistview(ListView):
    model=LaptopModel
    template_name='showlaptop.html'

class LaptopCreateView(CreateView):
    model=LaptopModel
    template_name='addlaptop.html'
    fields='__all__'
    success_url='/laptop/show'


class LaptopUpadteView(UpdateView):
    model=LaptopModel
    template_name='addlaptop.html'
    fields='__all__'
    success_url='/laptop/show'


class LaptopdeleteView(DeleteView):
    model=LaptopModel
    success_url='/laptop/show'
