from django.conf.urls import url    # include is adding then
from django.contrib import admin
from .views import(
    post_home,
    post_delete,
    post_update,
    post_edit,
    post_create,
    post_save,
    )
    

urlpatterns = [
    
    url(r'^$',post_home),
    url(r'^delete/$',post_delete),
    url(r'^update/$',post_update),
    url(r'^edit/$',post_edit),
    url(r'^create/$',post_create),
    url(r'^save/$',post_save),
   
]
