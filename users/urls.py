from django.urls import include, path
from . import views
from .views import UserList


urlpatterns = [
    # Using class based views - APIViews
    path('', UserList.as_view())
]