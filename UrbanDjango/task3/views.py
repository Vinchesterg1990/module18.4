from django.shortcuts import render

# Create your views here.

def platform(request):
    return render(request, 'platform_1.html')

def games(request):
    return render(request, 'games_1.html')

def cart(request):
    return render(request, 'cart_1.html')

