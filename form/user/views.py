from django.shortcuts import render, redirect
from user.models import students_ID
# Create your views here.
def user(request):
    if request.method =='POST':
        name=request.POST.get('user_name')
        d=request.POST.get('password')
        students_ID.objects.create(user_name=name,password=d)
        return redirect('view')
    return render(request,'user.html')
def view(request):
    v=students_ID.objects.all()
    return render(request,'view.html',{'b':v})
def summa(request,pk):
    x=students_ID.objects.filter(id=pk)
    if request.method == 'POST':
        name = request.POST.get('user_name')
        d = request.POST.get('password')
        students_ID.objects.filter(id=pk).update(user_name=name, password=d)
        return redirect('view')
    return render(request,'update.html',{'pv': x})
