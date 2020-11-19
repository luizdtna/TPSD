from django.contrib import admin
from django.urls import path, include
from processos.views import GeralViewSet, testeview, consulta_api
from rest_framework import routers


router = routers.DefaultRouter()

router.register('objetos', GeralViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('teste', testeview),
    path('consulta_objetos', consulta_api),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]