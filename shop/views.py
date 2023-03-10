from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product
from .recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     translations__slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    categories = Category.objects.all()
    related_images = product.related_images
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request,
                  'product/detail.html', # Changed this from product/detail.html to ogani/shop-details.html
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'categories': categories,
                   'related_images': related_images,
                   'recommended_products': recommended_products})



def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        products = Product.objects.filter(name__contains=searched)
        context = {
            "searched": searched,
            "products": products
        }
        return render(request, "product/search.html", context)
    else: 
        return render(request, "product/search.html")


def automobile_view(request):
    products = Product.objects.filter(category_id=10).all()
    return render(request, 'shop/automobile.html', {"products": products})

def supermarket_view(request):
    products = Product.objects.filter(category_id=1).all()
    return render(request, 'shop/supermarket.html', {"products": products})


def health_and_beauty_view(request):
    products = Product.objects.filter(category_id=2).all()
    return render(request, 'shop/health_and_beauty.html', {"products": products})

def home_and_office_view(request):
    products = Product.objects.filter(category_id=3).all()
    return render(request, 'shop/home_and_office.html', {"products": products})

def phones_and_tablets_view(request):
    products = Product.objects.filter(category_id=4).all()
    return render(request, 'shop/phones_and_tablets.html', {"products": products})

def computing_view(request):
    products = Product.objects.filter(category_id=5).all()
    return render(request, 'shop/computing.html', {"products": products})

def electronics_view(request):
    products = Product.objects.filter(category_id=6).all()
    return render(request, 'shop/electronics.html', {"products": products})

def fashion_view(request):
    products = Product.objects.filter(category_id=7).all()
    return render(request, 'shop/fashion.html', {"products": products})

def baby_products_view(request):
    products = Product.objects.filter(category_id=8).all()
    return render(request, 'shop/baby_products.html', {"products": products})

def gaming_view(request):
    products = Product.objects.filter(category_id=9).all()
    return render(request, 'shop/gaming.html', {"products": products})

def other_categories_view(request):
    products = Product.objects.filter(category_id=11).all()
    return render(request, 'shop/others.html', {"products": products})