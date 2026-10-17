from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("",                            views.login_view,        name="login_view"),
    path("register/",                   views.register_view,     name="register_view"),
    path("logout/",                     views.logout_view,       name="logout_view"),
    path("books/",                      views.book_list_view,    name="book_list_view"),
    path("books/add/",                  views.add_book_view,     name="add_book_view"),
    path("books/<int:book_id>/",        views.book_detail_view,  name="book_detail_view"),
    path("books/<int:book_id>/reserve/", views.reserve_book_view, name="reserve_book_view"),
    path("books/<int:book_id>/update/", views.update_book_view,  name="update_book_view"),
    path("books/<int:book_id>/delete/", views.delete_book_view,  name="delete_book_view"),
]