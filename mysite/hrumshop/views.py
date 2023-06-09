from django.shortcuts import render
from hrumshop.utils import *
from django.views.generic import ListView, DetailView


class Main(DataMixin, ListView):
    model = Product
    template_name = 'hrumshop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Страница'
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ProductsList(DataMixin, ListView):
    model = Product
    template_name = 'hrumshop/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category.objects.get(slug=self.kwargs['slug'])
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ProductDetail(DataMixin, DetailView):
    model = Product
    template_name = 'hrumshop/product.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def transport(request):
    return render(request, 'hrumshop/transport.html', {'name': 'Доставка'})


def about(request):
    return render(request, 'hrumshop/about.html', {'name': 'О сайте'})


def contact(request):
    return render(request, 'hrumshop/contact.html', {'name': 'Контакты'})
