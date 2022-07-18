from django.shortcuts import redirect, render
from .forms import EmpForm1,EmpForm2,AccForm
from .models import Emp,Account

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_emp1(request):
    if request.method=='POST':
        f=EmpForm1(request.POST)
        f.save()
        return redirect('/')
    else:
        context={'form':EmpForm1}
        return render(request, 'form.html',context)

def add_emp2(request):
    if request.method=='POST':
        f=EmpForm2(request.POST)
        f.save()
        return redirect('/')
    else:
        context={'form':EmpForm2}
        return render(request, 'form.html', context)

def add_account(request):
    if request.method=='POST':
        f=AccForm(request.POST)
        f.save()
        return redirect('/')
    else:
        context={'form': AccForm}
        return render(request, 'form.html', context)

def view_emp(request):
    el=Emp.objects.all()
    context={"el":el}
    return render(request, 'emplist.html', context)

def view_acc(request):
    al=Account.objects.all()
    context={"al":al}
    return render(request, 'acclist.html', context)