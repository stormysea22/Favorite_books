from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name="books_index"),
    path('create/', views.BookCreate.as_view(), name="books_create")
]