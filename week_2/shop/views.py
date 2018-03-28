from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Product
from .models import Category
# Create your views here.


class ProductListView(generic.ListView):

    template_name = 'product_list.html'  # Шаблон из Templates/product_list
    context_object_name = 'products'  # под каким именем передадутся данные в шаблон
    model = Product  # название Модели

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # передаем в словарь контекста список всех категорий
        return context

    def index(request):
        browser_info = request.META['HTTP_USER_AGENT']
        return HttpResponse("Привет! Я знаю много информации о твоем браузере {}".format(browser_info))


class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
