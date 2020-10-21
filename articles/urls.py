from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.articleList, name="list"),
    path('create/',views.article_create, name="create"),
    path('<str:slug>/',views.articleDetail, name="detail"),
]
 