from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import ProductCreate

import os
from .models import(
    Products, 
)

class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join('products', 'product_list.html')
    
    def get_queryset(self):
        query = super().get_queryset()
        product_type_name = self.request.GET.get('product_type_name', None)
        product_name = self.request.GET.get('product_name', None)

        if product_type_name:
            query = query.filter(
                product_type__name=product_type_name
            )
        if product_name:
            query = query.filter(
                name=product_name
            )
        order_by_stock = self.request.GET.get('order_by_stock', 0)
        if order_by_stock == '1':
            query = query.order_by('stock')
        elif order_by_stock == '2':
            query = query.order_by('-stock')
        return query
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_type_name'] = self.request.GET.get('product_type_name', '')
        context['product_name'] = self.request.GET.get('product_name', '')
        order_by_stock = self.request.GET.get('order_by_stock')
        if order_by_stock == '1':
            context['ascending'] = True
        elif order_by_stock == '2':
            context['descending'] = True
        return context

class ProductCreateView(LoginRequiredMixin, CreateView, ProductCreate):
    template_name = os.path.join('products', 'create_product.html')
    model = Products
    form_class = ProductCreate
    success_url = reverse_lazy('products:product_list')
    

    
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('products', 'delete_product.html')
    model = Products
    fields = "__all__"
    success_url = reverse_lazy('products:product_list')
    def delete_product(self,request, product_id):
        product = Products.objects.get(pk=product_id)
        product.delete()
        return redirect('product_list')  # 削除後にリダイレクトする場所の名前を適切に設定すること
    

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    template_name = os.path.join('products', 'update_product.html')
    model = Products
    fields = "__all__"
    success_url = reverse_lazy('products:product_list')
    def update_product(self,request, product_id):
        product = Products.objects.get(pk=product_id)
        product.update()
        return redirect('product_list')