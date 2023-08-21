from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<slug:post_slug>/', post_detail, name='post_detail'),
    path('category/<int:cat_id>/', category, name='category')
]
