from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def company_1(request):
    return render(request, 'company_1.html')

def company_2(request):
    return render(request, 'company_2.html')

def company_3(request):
    return render(request, 'company_3.html')

#=========================================
def product_1(request):
    return render(request, 'product_1.html')

def product_2(request):
    return render(request, 'product_2.html')

def product_3(request):
    return render(request, 'product_3.html')


#=====================================
def article_1(request):
    return render(request, 'article_1.html')

def article_2(request):
    return render(request, 'article_2.html')

def article_3(request):
    return render(request, 'article_3.html')
# Create your views here.
