from django.shortcuts import render
from .models import Pizza, Burger

# Create your views here.
def index(request):
    ctx = {'active_tab': 'tab1'}
    return render(request, 'food/index.html', ctx)

def contact(request):
    ctx = {'active_tab': 'tab5'}
    return render(request, 'food/contact.html', ctx)

def pizza(request):
    pizzas = Pizza.objects.all()
    ctx = {'active_tab': 'tab2', 'pizzas':pizzas}
    return render(request, 'food/pizza.html', ctx)

def burgers(request):
    burgers = Burger.objects.all()
    ctx = {'active_tab': 'tab3', 'burgers':burgers}
    return render(request, 'food/burgers.html', ctx)