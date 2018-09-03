from django.shortcuts import render
from django.http import HttpResponse
from .models import create_profile
# Create your views here.
def home_view(request):
    return render(request,'Blogs/home.html')

def create_User_profile(request):
    return render(request,'Blogs/index.html')
    name = request.POST.get('user')
    print(name)
    useremail = request.POST.get('email')
    print(useremail)
    passw= request.POST.get('password')
    obj = create_profile()
    obj.user_name = name
    obj.email = useremail
    obj.password = passw
    obj.save()
    
    
