from django.urls import path

from . import views

app_name = "effector_database"
urlpatterns = [
    # Index pages
    path("", views.index, name="index"),
    path("search", views.search, name="search"),

    # Submit a new effector
    path("submit", views.submit, name="submit"),
    path("submitted", views.submitted, name="submitted"),

    # View/delete/update a single effector
    path("view/<str:effector_id>", views.view, name="view"),
    path("delete/<str:effector_id>", views.delete, name="delete"),
    path("update/<str:effector_id>", views.update, name="update"),
    path("updated/<str:effector_id>", views.updated, name="updated"),
]
