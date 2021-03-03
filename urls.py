from django.urls import path

from . import views

app_name = "effector_database"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("submitted", views.submitted, name="submitted"),
    path("search", views.search, name="search"),
    path("view/<str:effector_id>", views.view, name="view"),
    path("delete/<str:effector_id>", views.delete, name="delete"),
    path("update/<str:effector_id>", views.update, name="update"),
    path("updated/<str:effector_id>", views.updated, name="updated"),
]
