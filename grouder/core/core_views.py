from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

from item.item_models import Category, Item

from .core_forms import SingupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/core_index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/core_contact.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SingupForm()

    return render(request, 'core/core_signup.html', {
        'form': form
    })

def logout(request):
    auth_logout(request)
    return redirect('/')
    