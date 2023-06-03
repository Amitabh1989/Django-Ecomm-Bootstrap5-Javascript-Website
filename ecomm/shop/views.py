from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from shop.models import Product, Order
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
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

# class CheckOutView(TemplateView):
class CheckOutView(TemplateView):
    # template_name = reverse_lazy("shop:checkout")
    template_name = 'checkout.html'
    
    def post(self, request, *args, **kwargs):
        print(f"I got here : {request}")
        # Retrieve the form data
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "213")
        city = request.POST.get('city', "")
        address = request.POST.get('address', "")
        items = request.POST.get('items', "")
        totalPrice = request.POST.get('totalPrice', "")


        # Debug statements
        print("Name:", name)
        print("Email:", email)
        print("State:", state)
        print("Zipcode:", zipcode)
        print("City:", city)
        print("Address:", address)
        print("Items:", items)
        print("TotalPrice:", totalPrice)
        # Process the form data
        # ... perform any necessary operations with the data
        order = Order(name=name, email=email, address=address, zipcode=zipcode, city=city, state=state, items=items, totalPrice=totalPrice)
        order.save()

        # Redirect to a success page or render a template
        # Generate the URL for the success page
        success_url = reverse_lazy('shop:success')  # Replace 'success-page' with the actual URL name or path

        # Redirect to the success page
        return redirect(success_url)

class SuccessPageView(TemplateView):
    template_name = 'success.html'  # Replace 'success.html' with the template for your success page