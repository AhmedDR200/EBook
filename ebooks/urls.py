from django.urls import path
from .views import *

urlpatterns = [
    path('ebooks/', EbookListCreate.as_view(), name="list-create"),
    path('ebooks/<int:pk>/', EbookDetail.as_view(), name='ebook-detail'),
    path('reviews/', Reviews.as_view(), name="reviews"),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name="reviews-detail"),
]
