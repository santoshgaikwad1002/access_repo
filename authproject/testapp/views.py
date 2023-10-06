from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_view(request):
    return render(request,'testapp/javaexam.html')

@login_required
def python_view(request):
    return render(request,'testapp/pythonexam.html')

@login_required
def aptitude_view(request):
    return render(request,'testapp/aptitude.html')

def logout_view(request):
    return render(request,'testapp/logout.html')


from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
def signup_form_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        #form.save()
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'testapp/signup.html',{'form':form})
    
