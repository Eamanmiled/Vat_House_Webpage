from django.shortcuts import render

def home_page(request):
    return render(request, 'app1/home_page.html')

def about(request):
    return render(request, 'app1/about.html')

def entertainment(request):
    return render(request, 'app1/entertainment.html')

def food(request):
    return render(request, 'app1/food.html')

def location(request):
    return render(request, 'app1/location.html')

def whisky(request):
    return render(request, 'app1/whisky.html')
