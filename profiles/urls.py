from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path(r'^(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    path('<username>/', views.profile, name='profile'),
]