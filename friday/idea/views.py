from django.shortcuts import render,redirect
from idea.models import first_image

# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES['photo'] and request.FILES['book'] and request.FILES['clip']:
        w= request.POST.get('name')
        e= request.FILES['photo']
        r= request.FILES['book']
        t= request.FILES['clip']
        first_image.objects.create(Name=w,Photo=e,Book=r,Clip=t)
        return redirect('idea_view')
    return render (request,'home.html')

def idea_view(request):
    r=first_image.objects.all()
    return render (request,'idea_view.html', {'pv':r})


