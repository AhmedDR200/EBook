from django.urls import path
from . import views

urlpatterns = [
    path('ebooks/', views.EbookListCreate.as_view(), name="list-create"),
]
