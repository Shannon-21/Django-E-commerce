from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.item_models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/dashboard_index.html', {
        'items': items,
    })
