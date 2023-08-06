# from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.utils.translation import gettext_lazy as _
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home_view'),
    path('', include('bots.urls')),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'), 
    path('password/', change_password, name='change_password'),
    # path('generate/', generate_response, name='generate_response'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
