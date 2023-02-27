from django.urls import path
from .views import AllFeeds

# urlpatterns = [
#     path("", AllFeeds.as_view()),
#     path("<str:username", AllFeeds.as_view())
# ]

from . import views

urlpatterns = [
    path("", views.AllFeeds.as_view()),
    path("<str:username>", views.FeedDetail.as_view())
]
