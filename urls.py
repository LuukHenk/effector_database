from django.urls import path

from . import views

app_name = "effector_database"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("submitted", views.submitted, name="submitted"),
    path("search", views.search, name="search"),
    path("itemViewer/<str:item_name>", views.itemViewer, name="itemViewer"),
    path("deleteItem/<str:item_name>", views.deleteItem, name="deleteItem"),
    path("editItem/<str:item_name>", views.editItem, name="editItem"),
    path("updatedItem/<str:item_name>", views.updatedItem, name="updatedItem"),
]
