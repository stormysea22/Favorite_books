from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name="books_index"),
    path('<int:book_id>', views.book_detail, name="books_detail"),
    path('create/', views.BookCreate.as_view(), name="books_create"),
    path('<int:pk>/edit', views.BookEdit.as_view(), name="books_edit"),
    path('<int:pk>/delete', views.BookDelete.as_view(), name="books_delete"),
    path('<int:book_id>/make_favorite', views.make_favorite, name="make_favorite"),
    path('<int:book_id>/un_favorite', views.un_favorite, name="un_favorite"),
]