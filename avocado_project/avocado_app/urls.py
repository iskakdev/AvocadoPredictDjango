from django.urls import path
from .views import AvocadoPredict

urlpatterns = [
    path('predict/', AvocadoPredict.as_view(), name='avocado_predict')
]