from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name="homepage"),
    path('full-analysis', views.full_analysis, name="full-analysis"),
    path('sector-wise-analysis', views.sector_wise_analysis, name="sector-wise-analysis"),
    path('prediction', views.prediction, name="prediction"),


]
