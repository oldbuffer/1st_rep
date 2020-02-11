from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "partial/home.html")

def single(request):
    return render(request, "partial/single.html")