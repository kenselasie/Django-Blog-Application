from django.urls import include, path
from . import views
from .views import PostList


urlpatterns = [
    # Using class based views - APIViews
    path('', PostList.as_view())
]