"""
URL configuration for finchcollector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from main_app.views import index, details, FinchCreateView, FinchUpdateView, FinchDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('finch/<int:finch_id>/', details, name='details'),
    path('finch/create/', FinchCreateView.as_view(), name='create'),
    path('finch/update/<int:pk>/', FinchUpdateView.as_view(), name='update'),
    path('finch/delete/<int:pk>/', FinchDeleteView.as_view(), name='delete'),
]
