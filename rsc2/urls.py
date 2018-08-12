"""rsc2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the catalog application 
from django.conf.urls import include
from django.urls import path

urlpatterns += [
    path('scheduler/', include('scheduler.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/scheduler/')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #path('accounts/logout', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
