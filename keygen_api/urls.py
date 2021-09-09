from django.contrib import admin
from django.urls import path,include
from crud import views
from rest_framework import routers

# registering route to serialized data 
router = routers.DefaultRouter()
router.register(r'keys', views.KeyView, 'index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('form/',views.form,name="form"),
    path('api/', include(router.urls)),
]


