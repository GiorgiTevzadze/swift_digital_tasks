from django.urls import path
from .views import ShortenerAPIView, RedirectShortenerAPIView

urlpatterns = [
    path('test/', ShortenerAPIView.as_view()),
    path('<slug:short_code>/', RedirectShortenerAPIView.as_view())
]
