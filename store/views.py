from django.shortcuts import get_object_or_404, render, redirect

from .models import Category, Product, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'product': product})




def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Set the user before saving
            review.save()

            messages.success(request, 'Review added successfully!')
            return redirect('store:success_page')
        else:
            messages.error(request, 'Error in form submission. Please check your input.')
    else:
        form = ReviewForm()

    return render(request, 'store/add_review.html', {'form': form})

from django.shortcuts import render

def success_page(request):
    return render(request, 'store/success_page.html')
