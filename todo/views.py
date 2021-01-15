from django.shortcuts import render, HttpResponse

# Create your views here.
def get_todo_list(request):
    # return HttpResponse("Hello")
    return render(request, 'todo/todo_list.html')
