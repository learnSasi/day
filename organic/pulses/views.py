from django.shortcuts import render,redirect

# Create your views here.
from pulses.models import snacks,vendor


def h1(request):
    a=snacks.objects.all()
    return render(request,'master/h1.html',{'b':a})

def login(request):
    return render(request,'master/login.html')
def start(request):

    if request.method == 'POST' and request.FILES['product_image']:
        q = request.FILES['product_image']
        w = request.POST.get('product_name')
        e = request.POST.get('product_code')
        r = request.POST.get('price')
        t = request.POST.get('description')
        y = request.POST.get('health_benefits')
        snacks.objects.create(product_image=q,product_name=w,product_code=e,price=r,description=t,health_benefits=y)
        return redirect('view_p')
    return render(request,'master/start.html')

def view_p(request):
    w=snacks.objects.all()
    return render(request,'master/view_p.html',{'b':w})

def update_p(request,pk):
    w= snacks.objects.filter(id=pk)
    if request.method == 'POST' and request.FILES['product_image']:
        q = request.FILES['product_image']
        w = request.POST.get('product_name')
        e = request.POST.get('product_code')
        r = request.POST.get('price')
        t = request.POST.get('description')
        y = request.POST.get('health_benefits')
        snacks.objects.filter(id=pk).update(product_image=q, product_name=w, product_code=e, price=r,description=t,health_benefits=y)
        return redirect('view_p')
    return render(request,'master/update_p.html',{'b':w})

def delete_p(request,pk):
    snacks.objects.filter(id=pk).delete()
    w = snacks.objects.all()
    return render(request,'master/delete_p.html',{'b':w})

