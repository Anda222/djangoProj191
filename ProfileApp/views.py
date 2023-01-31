from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request,'profile.html')

def education(request):
    return render(request,'education.html')

def attention(request):
    return render(request,'attention.html')

def career(request):
    return render(request, 'career.html')

def idol(request):
    return render(request,'idol.html')