from django.shortcuts import get_object_or_404, render
from .models import Category, Item

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'store/index.html', context)

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    context = {
        'item': item
    }

    return render(request, 'store/item.html', context)
    