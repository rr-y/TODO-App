from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .form import CreatNewList, CreateNewItem
# Create your views here.


def index(request, id):
    obj = ToDoList.objects.get(id = id)
    if request.method == "POST":
        if request.POST.get("save"):
            for item in obj.item_set.all():
                if request.POST.get("c"+str(item.id)) == "clicked":
                    if not item.completed:
                        item.completed = True
                    else:
                        item.completed = False
                    item.save()

        elif request.POST.get("newItem"):
            text = request.POST.get("new")
            obj.item_set.create(text=text)

    return render(request, "list.html", {"obj":obj})


def home(request):
    return render(request, "home.html", {})


def create(request):
    if request.method == 'POST':
        print("Hello")
        form = CreatNewList(request.POST)
        if form.is_valid():
            print("valid form")
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
            return HttpResponseRedirect("/%i" %t.id)
    form = CreatNewList()
    return render(request, "create.html", {"form":form})


def view(request):
    return render(request, "view.html", {})
