from django.shortcuts import render
from product.models import Product , Category
# Create your views here.


def home(request):
    
    all_category = Category.objects.all() 
    products = Product.objects.all()

    template = 'home/home.html'
    context = { 'all_category' : all_category , 'products' : products}

    return render(request , template , context)

def category_page(request,cate):
    print(str(cate))
    category = Category.objects.get(category_name=cate)
    products=Product.objects.filter(category=category)
    return render(request,'home/category_page.html',{'products':products})

def single_item(request,item):
    product=Product.objects.filter(name=item)
    return render(request,'home/single_item.html',{'product':product[0]})


def index(request):
    context_dict={
        'mobiles':'mobiles',
        'electronics':'electronics',
        'cars':'cars',
        'bikes':'bikes',
        'furnitures':'furnitures',
        'pets':'pets',
        'books':'books',
        'fashion':'fashion',
        'kids':'kids',
        'services':'services',
        'jobs':'jobs',
        'realestate':'realestate',
    }
    return render(request,'home/index.html',context=context_dict)


def contact(request):
    return render(request, 'minor_pages/contact.html')

def faq(request):
    return render(request, 'minor_pages/faq.html')

def feedback(request):
    return render(request, 'minor_pages/feedback.html')

def howitworks(request):
    return render(request, 'minor_pages/howitworks.html')

def privacy(request):
    return render(request, 'minor_pages/privacy.html')

