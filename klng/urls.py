from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('portfolio/', views.PortfolioList.as_view(), name='portfolio_list'),
    path('portfolio/<int:pk>', views.PortfolioDetail.as_view(), name='portfolio_detail'),
    path('project/', views.ProjectList.as_view(), name='project_list'),
    path('project/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),

]