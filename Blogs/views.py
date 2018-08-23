from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request,'Blogs/home.html')

def create_profile(request):
    return render(request,'Blogs/index.html')
