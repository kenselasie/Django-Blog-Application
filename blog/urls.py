from django.urls import include, path
from . import views
from .views import PostsView


urlpatterns = [
    # Using class based views - APIViews
    path('', PostsView.as_view())
]