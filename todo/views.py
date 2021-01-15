from django.shortcuts import render, HttpResponse
from .models import Item
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    # return HttpResponse("Hello")
    return render(request, 'todo/todo_list.html', context)
