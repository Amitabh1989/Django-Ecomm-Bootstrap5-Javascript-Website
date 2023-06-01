from django.shortcuts import render
from django.urls import reverse_lazy
from shop.models import Product
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

class ProductView(ListView):
    model = Product
    queryset = Product.objects.order_by('category')
    context_object_name = 'product_list'
    paginate_by = 4


    # This is the search code
    def get_queryset(self):
        query = self.request.GET.get('item_description')  # Retrieve the value of 'item_name' from the request
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(Q(description__icontains=query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], self.paginate_by)
        page = self.request.GET.get('page')
        products = paginator.get_page(page)
        context['product_list'] = products
        return context

class ProductDetailView(DetailView):
    model = Product

    # def get(self, request, *args, **kwargs):
    #     query = request.GET.get('item_description')  # Retrieve the value of 'item_name' from the request
    #     queryset = super().get_queryset()
    #     if query:
    #         queryset = queryset.filter(description__icontains=query)
    #     return queryset