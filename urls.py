from django.urls import path

from . import views

app_name = "database"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("submitted", views.submitted, name="submitted"),
    path("databaseViewer", views.databaseViewer, name="databaseViewer"),
    path("itemViewer/<str:item_name>", views.itemViewer, name="itemViewer"),
    path("deleteSequence", views.deleteSequence, name="deleteSequence"),
]
