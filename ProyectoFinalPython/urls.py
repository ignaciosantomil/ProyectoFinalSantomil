
from django.contrib import admin
from django.urls import path, include
from AppProyecto.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppProyecto/', include('AppProyecto.urls'))
]
