from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('upload/', views.create, name='create'),  # 이 줄 추가
    # path('hidden-photos/<int:pk>', views.detail, , kwargs={'hidden':True}),
]
