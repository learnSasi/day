from django.shortcuts import render,redirect

# Create your views here.
from customer.models import ppl, review
from pulses.models import snacks


def pulses(request):
    w = snacks.objects.all()
    search=''
    if request.method=='POST':
        c=request.POST.get('search')
        search=snacks.objects.filter(product_name=c)
    return render(request,'master/pulses.html', {'a':w ,'d':search})

def review_r(request):
    beta= request.session['unique']
    if request.method == 'POST':
        a=request.POST.get('rate')
        s=request.POST.get('review')
        review.objects.create(star=a,review=s,suma=beta)
    w= review.objects.all().order_by('-id')
    return render(request,'customer/review.html',{'b':w })

def mark(request,pk):
    aa=snacks.objects.get(id=pk)
    unid=aa.id
    request.session['unique']=unid
    d=snacks.objects.filter(id=unid)
    a=review.objects.filter(suma=unid)
    for i in d:
        nname=i.product_name
        snacks.objects.filter(product_name=nname)
    return render(request,'customer/select.html',{'pv':d ,'df':a})