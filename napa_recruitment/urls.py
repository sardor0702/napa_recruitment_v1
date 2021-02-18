"""napa_recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
<<<<<<< HEAD
import debug_toolbar
=======
from django.conf.urls.i18n import i18n_patterns
>>>>>>> 56a628b36c825bf243655400569390352e1394e5

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('user/', include('user.urls', namespace='user')),
=======
    # path('api/', include([
    #     path('user/', include('user.urls'))
    # ])),
    # path('', include('main.urls'))
]

urlpatterns += i18n_patterns(
    path('api/', include([
        path('user/', include('user.urls'))
    ])),
>>>>>>> 56a628b36c825bf243655400569390352e1394e5
    path('', include('main.urls'))
)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls'))
# ]
