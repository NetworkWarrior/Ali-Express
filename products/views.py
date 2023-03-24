from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Product, ProductReview
from .forms import ProductReviewForm, LocalProductForm
# Create your views here.


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        search_query = request.GET.get('q')
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) |
                Q(category__type__icontains=search_query) |
                Q(category__categories__icontains=search_query) |
                Q(company__name__icontains=search_query)
            )
        return render(request, 'products/products_list.html',{'products':products})


class ProductDetailView(LoginRequiredMixin, View):
    def get_paginator_page(self, request, queryset):
        page_size = request.GET.get('page_size', 1)
        paginator = Paginator(queryset, page_size)
        page_num = request.GET.get('page', 1)
        return paginator.get_page(page_num)

    def get(self, request, id):
        product = Product.objects.get(id=id)
        pictures = product.productpicture_set.all()
        page_obj = self.get_paginator_page(request, pictures)
        review_form = ProductReviewForm()
        return render(request, 'products/products_detail.html',
                      {'product': product, 'page_obj': page_obj, 'review_form': review_form})

    def post(self, request, id):
        product = Product.objects.get(id=id)
        review_form = ProductReviewForm(data=request.POST)
        pictures = product.productpicture_set.all()
        page_obj = self.get_paginator_page(request, pictures)
        if review_form.is_valid():
            ProductReview.objects.create(
                product=product,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse('products:product_detail', kwargs={'id': product.id}))
        messages.info(request, 'PLEASE CORRECT YOUR COMMENT FORM!!!')
        return render(request, 'products/products_detail.html',{'product': product, 'page_obj': page_obj, 'review_form': review_form})


class ProductPaymentView(View):
    def get(self, request):
        return render(request, 'products/payment.html')


class SellProductListView(View):
    def get(self, request):
        form = LocalProductForm()
        products = Product.objects.all()
        return render(request, 'products/sell_product.html', {'form':form, 'products':products})

    def post(self, request):
        form = LocalProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.set_user(request.user)
            form.save()
            messages.success(request, 'Your product has been added to the sale')
            return redirect('products:product_sell')
        else:
            context = {'form': form}
            return render(request, 'products/sell_product.html', context)

class SellProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        return render(request, 'products/detail_sell_product.html', {'product':product})







