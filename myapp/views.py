from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from myapp.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    items = Todo.objects.all().order_by('add_date')
    return render(request, 'index.html', {"todo_items": items})


@csrf_exempt
def add(request):
    curr_date = timezone.now()
    content = request.POST['data']
    created_object = Todo.objects.create(add_date=curr_date, text=content)

    return HttpResponseRedirect('/')


@csrf_exempt
def delete(request, id):
    Todo.objects.get(id=id).delete()

    return HttpResponseRedirect('/')
