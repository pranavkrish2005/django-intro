from django.urls import path
from reviews.views import MyReviews
from reviews.views import StoreMyReviews

urlpatterns = [
    path('reviews', MyReviews.as_view()),
    path('reviews_add', StoreMyReviews.as_view())
]