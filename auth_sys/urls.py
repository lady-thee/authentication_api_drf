from django.urls import path 
from . import views 



urlpatterns = [
    # path('', views.loadSignUp, name='api')
    path('', views.APIOverview.as_view()),
    # path('create/', views.APICreate.as_view())
    path('signup/', views.loadSignup),
    path('login/', views.loadLogin)
]