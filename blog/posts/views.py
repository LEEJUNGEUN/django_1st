from django.shortcuts import render

def home(request):
    return render(request, "posts/index.html")

# Create your views here.
