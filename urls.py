from django.urls import path

from . import views

app_name = "database"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("submitted", views.submitted, name="submitted"),
    path("search", views.search, name="search"),
    path("itemViewer/<str:item_name>", views.itemViewer, name="itemViewer"),
    path("deleteSequence/<str:item_name>", views.deleteSequence, name="deleteSequence"),
]
