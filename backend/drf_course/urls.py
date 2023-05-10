from django.urls import path
from core.views import ImportDataView, DetailModelView, DetailItemView
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = router.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', ImportDataView.as_view(), name='import'),
    path('detail/<str:model_name>/', DetailModelView.as_view(), name='detail-model'),
    path('detail/<str:model_name>/<int:pk>/', DetailItemView.as_view(), name='detail-item')
]