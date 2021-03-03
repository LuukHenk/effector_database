from django.urls import path

from . import views

app_name = "effector_database"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("submitted", views.submitted, name="submitted"),
    path("search", views.search, name="search"),
    path("itemViewer/<str:effector_id>", views.itemViewer, name="itemViewer"),
    path("deleteItem/<str:effector_id>", views.deleteItem, name="deleteItem"),
    path("editItem/<str:effector_id>", views.editItem, name="editItem"),
    path("updatedItem/<str:effector_id>", views.updatedItem, name="updatedItem"),
]
