from django.urls import path
from . import views
urlpatterns = [
    path('', views.messages_page),
    path("save/", views.save, name="save"),
    path("download/<str:file_name>", views.download, name="download"),
]

