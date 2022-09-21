"""busproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from busapp import views
from django.contrib import admin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('detail/', views.detail),
    # path('detail/create/', views.index),
    path('home/', views.empDetails,name="home"),
    path('signin/home/', views.empDetails,name="home"),
    path('create/', views.create_view),
    path('update/', views.update_view),
    path('delete/<id>', views.delete_view,name="delete"),
    path('update/<id>', views.update_view,name="update"),
    path('rough', views.rough,name="rough"),
    path('login', views.login,name="login"),
    path('signin/', views.signin,name="signin"),
    path('signup/', views.signup,name="signup"),
    path('signout', views.signout, name="signout"),
    path('homepage/', views.homepage,name="homepage"),
    # path('group/', views.busticket,name="busticket"),
    # path('driver/', views.driver,name="driver"),
    # path('driver/', views.driver,name="driver"),
    # path('user/', views. user_gains_perms,name="user"),
#     path('account/login/?next=/group1/', views.premiumProducts,name="premiumProducts"),
#     # path('create/' views.empDetails),
]
