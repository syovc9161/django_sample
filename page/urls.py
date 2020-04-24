from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('hidden-photos/<int:pk>', views.detail, , kwargs={'hidden':True}),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static('media', document_root=settings.MEDIA_ROOT)