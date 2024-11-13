

from django.shortcuts import render

# Create your views here.

def platform(request):
    return render(request, 'platform_1.html')

def cart(request):
    return render(request, 'cart_1.html')

def menu(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'games_1.html', context)

