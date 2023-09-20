"""
URL configuration for Students_Dropout project.

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
from django.contrib import admin
from django.urls import path
from myapp import views

admin.site.site_header = "Studens Dropout Admin"
admin.site.site_title = "Studens Dropout Portal"
admin.site.index_title = "Welcome to Studens Dropout Portal"
app_name = 'urls'
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('flot',views.flot,name='flot'),
    path('morris',views.morris,name='morris'),
    path('chartjs',views.chartjs,name='chartjs'),
    path('chartist',views.chartist,name='chartist'),
    path('sparkline',views.sparkline,name='sparkline'),
    path('peity',views.peity,name='peity'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('Uplod',views.Uplod,name='Uplod'),
    path('form',views.form,name='form'),
    path('URL',views.URL,name='URL'),
     path('Format',views.Format,name='Format'),
    
    path('excel',views.simple_upload,name='excel'),
    
    
]

