from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def index(request):
    return render(request,'home.html')
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        prodt=Product.objects.filter(category=c_page,available=True)
    else:
        prodt=Product.objects.all().filter(available=True)
    cat=Category.objects.all()
    paginator = Paginator(prodt,4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = Paginator.page(Paginator.num_pages)
    return render(request,"index.html",{'pr':prodt,'ct':cat,'products':products})
def ProdCatDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})
def searchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,"search.html",{'query':query,'products':products})