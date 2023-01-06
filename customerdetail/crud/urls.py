from django.contrib import admin  
from django.urls import path  
from crud import views


urlpatterns = [  
    path('admin/', admin.site.urls),  
    #path('emp', views.emp),  
    path('show',views.),  

] 
