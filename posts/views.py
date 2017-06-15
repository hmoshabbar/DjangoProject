from django.shortcuts import render
from django.http import HttpResponse
from .models import Register


# Create your views here.
def post_home(request):
    queryset=Register.objects.all()
    context={
        "all_list":queryset,
        "title":"Register"
        }
    return render(request,"index.html",context)

def post_delete(request):
    return HttpResponse("<h1>Delete </h1>")

def post_update(request):
    return HttpResponse("<h1>Update </h1>")

def post_create(request):
    return HttpResponse("<h1>Create </h1>")

def post_edit(request):
    return HttpResponse("<h1>Edit </h1>")

def post_save(request):
    return HttpResponse("<h1>Save</h1>")
