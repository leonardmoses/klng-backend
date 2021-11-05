from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.UserView.as_view(), name='user_view'),
    path('users/', views.UserView.as_view(), name='user_view'),
    path('users/<int:pk>', views.UserShow.as_view(), name='user_show'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio_view'),
    path('portfolio/<int:pk>', views.PortfolioShow.as_view(), name='portfolio_show'),
    path('project/', views.ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>', views.ProjectView.as_view(), name='project_show'),

]